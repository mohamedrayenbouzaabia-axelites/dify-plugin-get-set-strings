from collections.abc import Generator
from typing import Any
import json

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class GetStringsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        keys_param = tool_parameters.get("keys", [])

        # Normalize to list
        if isinstance(keys_param, str):
            try:
                keys = json.loads(keys_param)  # try parse string like '["a","b"]'
                if not isinstance(keys, list):
                    keys = [keys]
            except Exception:
                keys = [keys_param]
        elif isinstance(keys_param, list):
            keys = keys_param
        else:
            raise ValueError("keys must be a list or JSON string of strings")

        results = {}
        print(keys[0])
        for key in keys:
            value = self.session.storage.get(key)
            if value is not None:
                results[key] = value.decode()

        yield self.create_text_message(str(results))
