from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field


class EndpointMethod(str, Enum):
    GET = "get"
    POST = "post"
    DELETE = "delete"
    PUT = "put"
    PATCH = "patch"

class EndpointParameter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    description: Optional[str] = ""
    required: bool = False
    param_schema: Optional[dict] = Field(default_factory=dict, alias="schema")
    parameter_in: Optional[str] = Field(default_factory=str, alias="in")

class EndpointDetails(BaseModel):
    summary: Optional[str] = ""
    description: Optional[str] = ""
    operationId: Optional[str] = ""
    responses: Optional[dict] = {}

    @computed_field
    @property
    def docstring(self) -> str:
         return f"{self.summary}\n\n{self.description}".strip()

class Endpoint(BaseModel):
    path: str
    method: EndpointMethod
    details: EndpointDetails
    parameters: Optional[list[EndpointParameter]] = []
