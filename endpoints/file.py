import json
from collections.abc import Mapping

from flask import Request, Response
from dify_plugin import Endpoint


class FileEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:

        key = r.args.get("key")
        if not key:
            raise ValueError("key is required for get file")

        if settings.get("api_key") and settings.get("api_key") != r.args.get("api_key"):
            raise ValueError("api key not match")

        try:
            file_content = self.session.storage.get(f"{key}:content")
            meta_json = self.session.storage.get(f"{key}:meta").decode()
            meta = json.loads(meta_json)

            headers = {
                'Content-Type': meta['mime_type'],
                'Content-Disposition': f'attachment; filename="{meta["filename"]}"'
            }

            return Response(
                file_content,
                status=200,
                headers=headers
            )

        except Exception as e:
            return Response(f"Error: {str(e)}", status=404, content_type="text/plain")
