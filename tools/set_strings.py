from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class SetStringsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        kv_pairs: list[dict[str, str]] = tool_parameters.get("items", [])

        if not isinstance(kv_pairs, list):
            raise ValueError("items must be a list of {key, value} objects")

        for pair in kv_pairs:
            key = pair.get("key")
            value = pair.get("value")
            if not key or value is None:
                continue

            if tool_parameters.get("size") and len(value) > tool_parameters["size"]:
                raise ValueError(f"Value for key '{key}' is too large")

            self.session.storage.set(key, value.encode())

        yield self.create_text_message("SUCCESS: All strings set")
