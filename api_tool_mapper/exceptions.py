class InvalidJson(Exception):
    """When the JSON is invalid."""
    def __init__(self, message = "Invalid JSON."):
        self.message = message
        super().__init__(self.message)

class UnsupportedSpecFormat(Exception):
    """When the spec format is not supported."""
    def __init__(self, message = "Unsupported spec format. Supported format is only JSON."):
        self.message = message
        super().__init__(self.message)

class UnsupportedOpenAPIVersion(Exception):
    """When the OpenAPI version is not supported."""
    def __init__(self, message = "Unsupported OpenAPI version. Supported version is only 2.0 and 3.0."):
        self.message = message
        super().__init__(self.message)

class HostURLNotFound(Exception):
    """When the host URL is not found in the OpenAPI file."""
    def __init__(self, message = "Host URL not found in the OpenAPI file."):
        self.message = message
        super().__init__(self.message)
