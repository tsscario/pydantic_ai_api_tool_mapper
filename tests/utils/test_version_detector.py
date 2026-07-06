import pytest

from api_tool_mapper.utils.version_detector import detect_version
from api_tool_mapper.exceptions import UnsupportedOpenAPIVersion

def test_detect_version_2_0():
    spec = {
        "swagger": "2.0"
    }
    version = detect_version(spec)
    assert version == "2.0"

def test_detect_version_3_0():
    spec = {
        "openapi": "3.0.0"
    }
    version = detect_version(spec)
    assert version == "3.0"

def test_detect_version_3_1():
    spec = {
        "openapi": "3.1.0"
    }
    version = detect_version(spec)
    assert version == "3.1"

def test_detect_version_3_1_1():
    spec = {
        "openapi": "3.1.1"
    }
    version = detect_version(spec)
    assert version == "3.1"

def test_detect_version_unsupported():
    spec = {
        "openapi": "4.0.0"
    }
    with pytest.raises(UnsupportedOpenAPIVersion):
        detect_version(spec)
