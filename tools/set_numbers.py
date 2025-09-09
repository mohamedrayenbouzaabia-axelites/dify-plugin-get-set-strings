# tools/set_numbers.py
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetNumbersTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        kv_list = tool_parameters.get("list", [])
        for item in kv_list:
            key = item.get("key")
            value = item.get("value")
            if key and value is not None:
                self.session.storage.set(key, str(value).encode())
        yield self.create_text_message("SUCCESS")
