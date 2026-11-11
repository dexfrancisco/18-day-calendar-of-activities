import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_free_port(start_port=8080):
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
            port += 1
    return 8080

class StudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    
    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))

def main():
    port = find_free_port(8080)
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, StudioHandler)
    url = f"http://127.0.0.1:{port}/editor.html"
    
    print("=" * 65)
    print(" 🎨 18-DAY ORANGE CAMPAIGN — INTERACTIVE POSTER STUDIO")
    print("=" * 65)
    print(f" Server running at: {url}")
    print(" Opening interactive canvas editor in your default browser...")
    print(" Press Ctrl+C in this terminal to stop the studio server.")
    print("=" * 65)
    
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Could not automatically open browser: {e}")
        print(f"Please open this link manually in Chrome/Edge: {url}")
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Poster Studio server... Goodbye!")
        httpd.server_close()

if __name__ == "__main__":
    main()

