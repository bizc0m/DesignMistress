from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import sys

from build import build

build()
dist = Path(__file__).resolve().parent / "dist"
os.chdir(dist)
port = int(sys.argv[1]) if len(sys.argv) > 1 else 1420
print(f"Capsule locale : http://127.0.0.1:{port}", flush=True)
ThreadingHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler).serve_forever()
