# tools/set_number_if_not_exist.py
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetNumberIfNotExistTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        key = tool_parameters.get("key")
        value = tool_parameters.get("value")
        if self.session.storage.get(key) is None:
            self.session.storage.set(key, str(value).encode())
            yield self.create_text_message(f"SUCCESS: Key '{key}' was set.")
        else:
            yield self.create_text_message(f"SKIPPED: Key '{key}' already exists.")
