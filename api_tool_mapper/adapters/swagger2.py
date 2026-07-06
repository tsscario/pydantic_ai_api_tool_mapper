import json

from api_tool_mapper.constants import HTTP_METHODS
from api_tool_mapper.exceptions import HostURLNotFound
from api_tool_mapper.models import Endpoint, EndpointMethod, EndpointParameter, EndpointDetails

class Swagger2Adapter:

    def __init__(self, spec: dict):
        self._spec = spec

    def base_url(self) -> str:
        host = self._spec["host"]
        base_path = self._spec.get("basePath", "")
        scheme = self._spec.get("schemes", ["https"])[0]
        return f"{scheme}://{host}{base_path}".rstrip("/")

    def endpoints(self) -> list[Endpoint]:
        result = []
        for path, methods in self._spec.get("paths", {}).items():
            path_params = methods.get("parameters", [])  # parâmetros no nível do path
            for method, details in methods.items():
                if method in HTTP_METHODS:
                    all_params = path_params + details.get("parameters", [])
                    result.append(self._build_endpoint(path, method, details, all_params))
        return result

    def _build_endpoint(self, path: str, method: str, details: dict, all_params: list[dict]) -> Endpoint:
        return Endpoint(path=path, method=method, details=details, parameters=all_params)
