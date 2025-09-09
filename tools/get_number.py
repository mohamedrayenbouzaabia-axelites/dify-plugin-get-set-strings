# tools/get_number.py
import json
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetNumberTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        key = tool_parameters.get("key")
        value_bytes = self.session.storage.get(key)

        if value_bytes:
            try:
                # Use float to handle both integers and decimals
                num_value = float(value_bytes.decode())
                yield self.create_text_message(json.dumps({"value": num_value}))
            except (ValueError, TypeError):
                raise ValueError(f"Value for key '{key}' is not a valid number.")
        else:
             yield self.create_text_message(json.dumps({"value": None}))
