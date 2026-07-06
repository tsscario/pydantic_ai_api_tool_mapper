import pytest
from api_tool_mapper.api_tool import APIToolMapper
from api_tool_mapper.api_mapper import OpenAPIMap
from api_tool_mapper.utils import load_spec
from api_tool_mapper.utils import detect_version
from api_tool_mapper.exceptions import UnsupportedOpenAPIVersion

def test_api_tool_mapper():
    openapi_map = OpenAPIMap("tests/openapi_spec_files/pet.json")
    api_tool_mapper = APIToolMapper(openapi_map)
    assert api_tool_mapper is not None
    assert len(api_tool_mapper.tools) == 20
    assert api_tool_mapper.tools[0].name == "uploadFile"
    assert api_tool_mapper.tools[0].description == "uploads an image"


def test_api_tool_mapper_with_openapi_31():
    openapi_map = OpenAPIMap("tests/openapi_spec_files/openweatherAPI.json")
    api_tool_mapper = APIToolMapper(openapi_map)
    assert api_tool_mapper is not None
    assert len(api_tool_mapper.tools) == 1
    assert api_tool_mapper.tools[0].name == "getWeatherData"
    assert api_tool_mapper.tools[0].description == "Retrieve current weather, hourly forecast, and daily forecast based on latitude and longitude."
