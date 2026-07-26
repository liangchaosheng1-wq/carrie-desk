from http.server import HTTPServer, SimpleHTTPRequestHandler
import os, urllib.parse

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # 强制 /download 路径返回 carrie.html 作为附件下载
        if self.path.startswith('/download') or self.path.startswith('/dl'):
            filepath = '/workspace/carrie-desk/carrie.html'
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="carrie.html"')
            self.send_header('Content-Length', str(os.path.getsize(filepath)))
            self.end_headers()
            with open(filepath, 'rb') as f:
                self.wfile.write(f.read())
            return
        # 普通访问走默认逻辑
        return super().do_GET()

if __name__ == '__main__':
    os.chdir('/workspace/carrie-desk')
    server = HTTPServer(('0.0.0.0', 8001), Handler)
    print('Download server on :8001')
    server.serve_forever()
