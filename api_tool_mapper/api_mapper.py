from pathlib import Path

from api_tool_mapper.adapters.swagger2 import Swagger2Adapter
from api_tool_mapper.adapters.openapi30 import OpenAPI30Adapter
from api_tool_mapper.utils import load_spec, detect_version
from api_tool_mapper.models import Endpoint


ADAPTERS = {
    "2.0": Swagger2Adapter,
    "3.0": OpenAPI30Adapter,
    "3.1": OpenAPI30Adapter,
}

class OpenAPIMap:
    def __init__(self, source: str | Path | dict):
        spec = load_spec(source)
        version = detect_version(spec)
        self._adapter = ADAPTERS[version](spec)
        self.version = version

    @property
    def base_url(self) -> str:
        return self._adapter.base_url()

    @property
    def endpoints(self) -> list[Endpoint]:
        return self._adapter.endpoints()
