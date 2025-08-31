import json
import os
import psutil
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/drives'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            drives = self.get_drive_info()
            self.wfile.write(json.dumps(drives).encode('utf-8'))
        elif self.path.startswith('/api/meta'):
            drive = self.path.split('=')[1]
            meta = self.read_meta_file(drive)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(meta).encode('utf-8'))
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path.startswith('/api/save_meta'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            self.write_meta_file(data['drive'], data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode('utf-8'))
    
    def get_drive_info(self):
        drives = []
        for partition in psutil.disk_partitions(all=False):
            drive_info = {
                'drive': partition.device,
                'id': partition.device,
                'machineID': platform.node(),
                'name': '',
                'pc': platform.node(),
                'priority': 0,
                'timestamp': 0,
                'type': 'internal' if 'fixed' in partition.opts else 'external'
            }
            drives.append(drive_info)
        return drives

    def read_meta_file(self, drive):
        meta_file = os.path.join(drive, '.drive.meta')
        if os.path.exists(meta_file):
            with open(meta_file, 'r') as f:
                return json.load(f)
        return {}

    def write_meta_file(self, drive, data):
        meta_file = os.path.join(drive, '.drive.meta')
        with open(meta_file, 'w') as f:
            json.dump(data, f, indent=4)

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
