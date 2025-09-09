# tools/get_numbers_with_defaults.py
import json
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetNumbersWithDefaultsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        keys = tool_parameters.get("list", [])
        default_value = tool_parameters.get("default")
        results = []

        for key in keys:
            value_bytes = self.session.storage.get(key)
            if value_bytes:
                try:
                    num_value = float(value_bytes.decode())
                    results.append({"key": key, "value": num_value})
                except (ValueError, TypeError):
                    results.append({"key": key, "value": default_value})
            else:
                results.append({"key": key, "value": default_value})

        yield self.create_text_message(json.dumps(results))
