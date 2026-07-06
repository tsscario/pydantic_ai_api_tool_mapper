from api_tool_mapper.exceptions import HostURLNotFound
from api_tool_mapper.models import Endpoint
from api_tool_mapper.constants import HTTP_METHODS
from api_tool_mapper.adapters.swagger2 import Swagger2Adapter

class OpenAPI30Adapter(Swagger2Adapter):
    def __init__(self, spec: dict):
        self._spec = spec

    def base_url(self) -> str:
        servers = self._spec.get("servers", [])
        if not servers:
            raise HostURLNotFound()
        return servers[0]["url"]
