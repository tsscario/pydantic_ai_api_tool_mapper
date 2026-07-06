from api_tool_mapper.adapters.swagger2 import Swagger2Adapter
from api_tool_mapper.models import Endpoint

def test_swagger2_adapter():
    host = "petstore.swagger.io"
    base_path = "/v2"
    schemes = ["https"]
    spec = {
        "host": host,
        "basePath": base_path,
        "schemes": schemes
    }
    adapter = Swagger2Adapter(spec)
    assert adapter.base_url() == f"{schemes[0]}://{host}{base_path}"
    assert adapter.endpoints() == []

def test_swagger2_adapter_with_paths():
    host = "petstore.swagger.io"
    base_path = "/v2"
    schemes = ["https"]
    path = "/pets"
    method = "get"
    details = {"summary": "Get all pets", "responses": {"200": {"description": "A list of pets"}}}
    spec = {
        "host": host,
        "basePath": base_path,
        "schemes": schemes,
        "paths": {
            path: {
                method: details
            }
        }
    }
    adapter = Swagger2Adapter(spec)
    endpoints = [
      Endpoint(
        path=path,
        method=method,
        details=details
      )
    ]
    assert adapter.base_url() == f"{schemes[0]}://{host}{base_path}"
    assert adapter.endpoints() == endpoints

def test_swagger2_adapter_with_parameters():
    host = "petstore.swagger.io"
    base_path = "/v2"
    schemes = ["https"]
    parameters = [{"name": "limit", "in": "query", "type": "integer", "required": False}]
    details = {"summary": "Get all pets", "parameters": parameters}
    path = "/pets"
    method = "get"
    spec = {
        "host": host,
        "basePath": base_path,
        "schemes": schemes,
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

    adapter = Swagger2Adapter(spec)
    assert adapter.base_url() == f"{schemes[0]}://{host}{base_path}"
    assert adapter.endpoints() == endpoints
