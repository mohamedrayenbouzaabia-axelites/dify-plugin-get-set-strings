# tools/get_all_prefixes.py
import json
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetAllPrefixesTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # Assumes a .keys() method to retrieve all keys
        all_keys = self.session.storage.keys()
        prefixes = set()

        for key_bytes in all_keys:
            key = key_bytes.decode()
            if "_" in key:
                # Assuming prefix is the part before the first underscore
                prefix = key.split('_')[0] + '_'
                prefixes.add(prefix)

        yield self.create_text_message(json.dumps(list(prefixes)))
