from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetStringTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        if value:= self.session.storage.get(tool_parameters["key"]):
            yield self.create_text_message(value.decode())
