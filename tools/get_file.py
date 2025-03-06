import json
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetFileTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        key = tool_parameters["key"]
        if content:= self.session.storage.get(f"{key}:content"):
            meta = self.session.storage.get(f"{key}:meta").decode()
            yield self.create_blob_message(blob=content, meta=json.loads(meta))
