from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/download' or self.path == '/dl':
            filepath = '/workspace/carrie-desk/carrie.html'
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="carrie.html"')
            self.send_header('Content-Length', str(os.path.getsize(filepath)))
            self.end_headers()
            with open(filepath, 'rb') as f:
                self.wfile.write(f.read())
            return
        elif self.path == '/apk' or self.path == '/download-apk':
            filepath = '/workspace/Carrie工作台.apk'
            self.send_response(200)
            self.send_header('Content-Type', 'application/vnd.android.package-archive')
            self.send_header('Content-Disposition', 'attachment; filename="CarrieDesk.apk"')
            self.send_header('Content-Length', str(os.path.getsize(filepath)))
            self.end_headers()
            with open(filepath, 'rb') as f:
                self.wfile.write(f.read())
            return
        return super().do_GET()

if __name__ == '__main__':
    os.chdir('/workspace/carrie-desk')
    HTTPServer(('0.0.0.0', 8002), Handler).serve_forever()
