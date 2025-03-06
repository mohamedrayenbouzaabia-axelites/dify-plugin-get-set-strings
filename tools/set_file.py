from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetFileTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file = tool_parameters.get("file")
        key = tool_parameters["key"]
        size = tool_parameters.get("size")

        if size and file.size > size * 1024 * 1024:
            raise ValueError("File size too large")

        # save file content
        self.session.storage.set(f"{key}:content", file.blob)
        # save file meta
        self.session.storage.set(f"{key}:meta", file.model_dump_json().encode())
        yield self.create_text_message("SUCCESS")
