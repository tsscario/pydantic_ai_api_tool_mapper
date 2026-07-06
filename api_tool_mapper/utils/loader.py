import json
from pathlib import Path

from api_tool_mapper.exceptions import InvalidJson, UnsupportedSpecFormat

def load_spec(source: str | Path | dict) -> dict:
    if isinstance(source, dict):
        return source

    path = Path(source)
    text = path.read_text(encoding="utf-8")

    if path.suffix != ".json":
        raise UnsupportedSpecFormat(f"Unsupported spec format: {path.suffix}")

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise InvalidJson(f"Invalid JSON: {e}")

