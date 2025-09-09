# tools/set_strings_with_prefix.py
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SetStringsWithPrefixTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        prefix = tool_parameters.get("prefix", "")
        kv_list = tool_parameters.get("list", [])

        if not isinstance(kv_list, list):
            raise ValueError("list must be an array of {key, value} objects")

        for item in kv_list:
            key = item.get("key")
            value = item.get("value")
            if key and value is not None:
                full_key = f"{prefix}{key}"
                self.session.storage.set(full_key, str(value).encode())

        yield self.create_text_message("SUCCESS")
