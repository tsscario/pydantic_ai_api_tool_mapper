import pytest

from api_tool_mapper.utils.loader import load_spec
from api_tool_mapper.exceptions import UnsupportedSpecFormat, InvalidJson

def test_load_source_path():
    spec = load_spec("tests/openapi_spec_files/pet.json")
    assert spec is not None
    assert spec["swagger"] == "2.0"
    assert spec["info"]["title"] == "Swagger Petstore"
    assert spec["info"]["version"] == "1.0.7"

def test_load_source_dict():
    spec = load_spec({
        "swagger": "2.0",
        "info": {
            "title": "Swagger Petstore",
            "version": "1.0.7"
        }
    })
    assert spec is not None
    assert spec["swagger"] == "2.0"
    assert spec["info"]["title"] == "Swagger Petstore"
    assert spec["info"]["version"] == "1.0.7"

def test_load_spec_yaml():
    with pytest.raises(UnsupportedSpecFormat):
        load_spec("tests/openapi_spec_files/pet.yaml")

def test_load_invalid_json():
    with pytest.raises(InvalidJson):
        load_spec("tests/openapi_spec_files/invalid.json")


