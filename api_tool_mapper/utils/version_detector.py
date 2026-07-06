from packaging.version import Version

from api_tool_mapper.exceptions import UnsupportedOpenAPIVersion

def detect_version(spec: dict) -> str:
    if "swagger" in spec:
        return "2.0"
    if "openapi" in spec:
        version = Version(spec["openapi"])

        if version >= Version("3.1") and version < Version("3.2"):
            return "3.1"

        if version >= Version("3.0") and version < Version("3.1"):
            return "3.0"

    raise UnsupportedOpenAPIVersion()
