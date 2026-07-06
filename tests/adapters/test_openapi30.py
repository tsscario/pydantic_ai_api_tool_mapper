from api_tool_mapper.adapters.openapi30 import OpenAPI30Adapter
from api_tool_mapper.models import Endpoint

def test_openapi30_adapter():
    server_url = "https://www.weatherapi.com/v1"
    spec = {
        "servers": [{"url": server_url}]
    }
    adapter = OpenAPI30Adapter(spec)
    assert adapter.base_url() == server_url
    assert adapter.endpoints() == []

def test_openapi30_adapter_with_paths():
    server_url = "https://www.weatherapi.com/v1"
    path = "/current.json"
    method = "get"
    details = {"summary": "Get current weather", "responses": {"200": {"description": "Current weather"}}}
    spec = {
        "servers": [{"url": server_url}],
        "paths": {
            path: {
                method: details
            }
        }
    }
    adapter = OpenAPI30Adapter(spec)
    endpoints = [
      Endpoint(
        path=path,
        method=method,
        details=details
      )
    ]
    assert adapter.base_url() == server_url
    assert adapter.endpoints() == endpoints

def test_openapi30_adapter_with_parameters():
    server_url = "https://www.weatherapi.com/v1"
    parameters = [{"name": "q", "in": "query", "type": "string", "required": True}]
    details = {"summary": "Get current weather", "parameters": parameters}
    path = "/current.json"
    method = "get"
    spec = {
        "servers": [{"url": server_url}],
        "paths": {
            path: {
                method: details
            }
        }
    }
    endpoints = [
      Endpoint(
        path=path,
        method=method,
        details=details,
        parameters=parameters
      )
    ]

    adapter = OpenAPI30Adapter(spec)
    assert adapter.base_url() == server_url
    assert adapter.endpoints() == endpoints
