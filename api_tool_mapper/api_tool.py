import json
import httpx
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field, create_model
from pydantic_ai import RunContext, Tool

class _ParamsBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

class APIToolMapper:
    def __init__(self, openapi_map):
        self.openapi_map = openapi_map
        self.tools = []
        self.convert_endpoints_to_tools()

    def convert_endpoints_to_tools(self):
        self.tools = []
        for endpoint in self.openapi_map.endpoints:
            self.tools.append(self.convert_endpoint_to_tool(endpoint))

    def convert_endpoint_to_tool(self, endpoint):
        param_model = self.create_model(endpoint)
        base_url = self.openapi_map.base_url
        path = endpoint.path
        method = endpoint.method
        parameters = endpoint.parameters

        async def tool_function(
            ctx: RunContext[dict[str, Any]],
            params: param_model,
        ) -> str:
            kwargs = params.model_dump(exclude_none=True)
            kwargs.update({k: v for k, v in ctx.deps.get("params", {}).items() if v is not None})

            url = f"{base_url}{path}"
            path_params: dict[str, Any] = {}
            query_params: dict[str, Any] = {}

            for param in parameters:
                p_name = param.name
                p_in = param.parameter_in
                if p_name not in kwargs:
                    continue
                if p_in == "path":
                    path_params[p_name] = kwargs[p_name]
                elif p_in == "query":
                    query_params[p_name] = kwargs[p_name]

            if path_params:
                url = url.format(**path_params)

            headers = ctx.deps.get("headers", {})
            async with httpx.AsyncClient() as client:
                if method.lower() == "get":
                    response = await client.get(url, params=query_params, headers=headers)
                elif method.lower() == "post":
                    response = await client.post(url, json=query_params, headers=headers)
                else:
                    return f"Erro: Método {method} não suportado neste exemplo."

                response.raise_for_status()
                return json.dumps(response.json(), ensure_ascii=False)

        return Tool(
            tool_function,
            name=endpoint.details.operationId,
            description=endpoint.details.docstring,
        )

    def create_model(self, endpoint):
        model_name = f"Params_{endpoint.details.operationId}"
        fields = self.convert_parameters_to_fields(endpoint.parameters)
        ParamModel = create_model(model_name, __base__=_ParamsBase, **fields)

        return ParamModel

    def openapi_type_to_python(self, openapi_type: str) -> type:
        if openapi_type == "integer":
            return int
        if openapi_type == "number":
            return float
        if openapi_type == "boolean":
            return bool
        return str

    def convert_parameters_to_fields(self, parameters):
        fields: dict[str, tuple[type, Any]] = {}

        for param in parameters:
            param_type = param.param_schema.get("type", "string")
            py_type = self.openapi_type_to_python(param_type)

            if param.required:
                fields[param.name] = (py_type, Field(description=param.description))
            else:
                fields[param.name] = (py_type | None, Field(default=None, description=param.description))

        return fields
