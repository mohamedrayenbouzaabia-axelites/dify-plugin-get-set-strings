from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetStringTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        if tool_parameters.get("size") and len(tool_parameters["value"]) > tool_parameters["size"]:
            raise ValueError("String size too large")
        self.session.storage.set(tool_parameters["key"], tool_parameters["value"].encode())
        yield self.create_text_message("SUCCESS")
