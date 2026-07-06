from typing import Protocol, runtime_checkable
from api_tool_mapper.models import Endpoint

class OpenAPIAdapter(Protocol):
    """contract that every OpenAPI adapter must comply with."""
    def base_url(self) -> str:
        """returns the base URL of the API (ex: https://petstore.swagger.io/v2)."""
        ...

    def endpoints(self) -> list[Endpoint]:
        """returns all endpoints normalized to the canonical model."""
        ...

    def info(self) -> dict:
        """metadata of the API (title, version, description)."""
        ...
