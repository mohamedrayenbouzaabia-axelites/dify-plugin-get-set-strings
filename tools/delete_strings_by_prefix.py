# tools/delete_strings_by_prefix.py
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class DeleteStringsByPrefixTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        prefix = tool_parameters.get("prefix", "")

        # Assumes a scan_keys method exists to find keys by pattern
        matching_keys = self.session.storage.scan_keys(f"{prefix}*")

        deleted_count = 0
        for key in matching_keys:
            self.session.storage.delete(key)
            deleted_count += 1

        yield self.create_text_message(f"SUCCESS: Deleted {deleted_count} items.")
