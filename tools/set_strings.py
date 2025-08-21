import json
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class SetStringsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            kv_pairs = json.loads(tool_parameters.get("items", "[]"))
        except Exception as e:
            raise ValueError(f"Invalid JSON for items: {e}")
       
        if not isinstance(kv_pairs, list):
            raise ValueError("items must be a JSON list of {key, value}")
     
        for pair in kv_pairs:
            key, value = next(iter(pair.items()))
            if not key or value is None:
                continue
            if tool_parameters.get("size") and len(value) > tool_parameters["size"]:
                raise ValueError(f"Value for key '{key}' is too large")
            self.session.storage.set(key, value.encode())
            

        yield self.create_text_message("SUCCESS: All strings settt")