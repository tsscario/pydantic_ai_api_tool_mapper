# Pydantic AI API Tool Mapper

Converts API definitions into tools for Pydantic AI agents

## Get started

```sh
uv init
uv sync
```

## How it works

This library has two main parts. First convert the API spec to models with class `OpenAPIMap`, second is convert the mapped APIs to agent tools with class `APIToolMapper`

## Supported API specification formats

Only `JSON` in `swagger 2.0`, `openAPI 3.0` and `openAPI 3.1`

## Exemplo de uso

```python

from pydantic_ai import Agent

from api_tool_mapper.api_tool import APIToolMapper

openapi_map = OpenAPIMap("tests/openapi_spec_files/openweatherAPI.json")
api_tool_mapper = APIToolMapper(openapi_map)

agent = Agent(
    model='openai:gpt-4o',
    instructions="You are a helpful assistant.",
    tools=api_tool_mapper.tools
)
```



## Learn more

- [Pydantic AI Agent Tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/)

