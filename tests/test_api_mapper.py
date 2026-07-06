import pytest
import json
from pathlib import Path

from api_tool_mapper.api_mapper import OpenAPIMap
from api_tool_mapper.exceptions import UnsupportedOpenAPIVersion

def test_api_mapper():
    openapi_map = OpenAPIMap("tests/openapi_spec_files/pet.json")
    assert openapi_map is not None
    assert openapi_map.base_url == "https://petstore.swagger.io/v2"
    assert openapi_map.version == "2.0"

def test_api_mapper_with_openapi_31():
    openapi_map = OpenAPIMap("tests/openapi_spec_files/openweatherAPI.json")
    assert openapi_map is not None
    assert openapi_map.base_url == "https://api.openweathermap.org"
    assert openapi_map.version == "3.1"

def test_api_mapper_with_invalid_version():
    with pytest.raises(UnsupportedOpenAPIVersion):
        OpenAPIMap("tests/openapi_spec_files/invalid_version.json")
