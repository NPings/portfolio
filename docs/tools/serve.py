# serve.py [port]: local demo server for this repo with HTTP byte-range support.
# `python3 -m http.server` ignores Range headers and answers 200 with the whole file. Apple's media stack
# (Safari and every iOS browser, including Firefox iOS, which is WebKit) expects 206 Partial Content for <video>;
# GitHub Pages already sends 206, so this keeps local demos honest. Run from the repo root.
import http.server, os, re, sys

class RangeHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_GET(self):
        path = self.translate_path(self.path)
        m = re.match(r'bytes=(\d*)-(\d*)$', self.headers.get('Range', '').strip())
        if not m or not os.path.isfile(path) or (not m.group(1) and not m.group(2)):
            return super().do_GET()
        size = os.path.getsize(path)
        if m.group(1):
            start = int(m.group(1)); end = int(m.group(2)) if m.group(2) else size - 1
        else:
            start = max(0, size - int(m.group(2))); end = size - 1
        end = min(end, size - 1)
        if start >= size or start > end:
            self.send_response(416); self.send_header('Content-Range', f'bytes */{size}')
            self.send_header('Content-Length', '0'); self.end_headers(); return
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length', str(end - start + 1))
        self.end_headers()
        with open(path, 'rb') as f:
            f.seek(start); self.wfile.write(f.read(end - start + 1))

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f'serving {os.getcwd()} on http://0.0.0.0:{port} (byte ranges on)', flush=True)
    http.server.ThreadingHTTPServer(('0.0.0.0', port), RangeHandler).serve_forever()
