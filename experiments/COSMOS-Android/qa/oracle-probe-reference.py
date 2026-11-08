#!/usr/bin/env python3
"""Optional dedicated Oracle HTTPS probe backend, not a Starve.io proxy.

Run behind your own HTTPS reverse proxy. Bind to loopback so that this port is
not exposed to the internet. Set COSMOS_ALLOWED_ORIGIN to the exact public
COSMOS URL (no slash). No user data is stored or logged by this app.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone

ALLOWED_ORIGIN = os.environ.get("COSMOS_ALLOWED_ORIGIN", "https://elyxion-cosmos-stage.vercel.app")


class Probe(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlsplit
        path = urlsplit(self.path).path
        if path not in ("/ping", "/health"):
            self.send_error(404)
            return
        body = json.dumps({"ok": True, "version": "cosmos-0.1", "serverTime": datetime.now(timezone.utc).isoformat()}, separators=(',', ':')).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        if self.headers.get("Origin") == ALLOWED_ORIGIN:
            self.send_header("Access-Control-Allow-Origin", ALLOWED_ORIGIN)
            self.send_header("Vary", "Origin")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # No request details or IP addresses are persisted by this app.


if __name__ == "__main__":
    port = int(os.environ.get("COSMOS_PORT", "8787"))
    ThreadingHTTPServer(("127.0.0.1", port), Probe).serve_forever()
