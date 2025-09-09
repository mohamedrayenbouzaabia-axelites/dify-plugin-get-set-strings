# tools/get_number_with_default.py
import json
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetNumberWithDefaultTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        key = tool_parameters.get("key")
        default_value = tool_parameters.get("default")
        value_bytes = self.session.storage.get(key)

        if value_bytes:
            try:
                num_value = float(value_bytes.decode())
                yield self.create_text_message(json.dumps({"value": num_value}))
            except (ValueError, TypeError):
                yield self.create_text_message(json.dumps({"value": default_value}))
        else:
            yield self.create_text_message(json.dumps({"value": default_value}))
