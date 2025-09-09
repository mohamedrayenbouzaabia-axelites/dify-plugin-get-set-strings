# tools/get_numbers_with_prefix_with_defaults.py
import json
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetNumbersWithPrefixWithDefaultsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        prefix = tool_parameters.get("prefix", "")
        default_value = tool_parameters.get("default")
        results = []

        matching_keys = self.session.storage.scan_keys(f"{prefix}*")

        for key_bytes in matching_keys:
            key = key_bytes.decode()
            value_bytes = self.session.storage.get(key)

            try:
                num_value = float(value_bytes.decode())
                results.append({"key": key.removeprefix(prefix), "value": num_value})
            except (ValueError, TypeError, AttributeError):
                results.append({"key": key.removeprefix(prefix), "value": default_value})

        yield self.create_text_message(json.dumps(results))
