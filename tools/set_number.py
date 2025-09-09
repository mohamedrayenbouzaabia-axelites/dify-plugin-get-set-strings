# tools/set_number.py
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetNumberTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        key = tool_parameters.get("key")
        value = tool_parameters.get("value")
        self.session.storage.set(key, str(value).encode())
        yield self.create_text_message("SUCCESS")
