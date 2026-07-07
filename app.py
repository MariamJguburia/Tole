import http.server
import socketserver
import os
import webbrowser

# Define the port to run the server on
PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and prevent browser caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()


class ReusableTCPServer(socketserver.TCPServer):
    # Allows the server to restart quickly without "Address already in use" errors
    allow_reuse_address = True


def run_server():
    # Ensure the script runs in the directory where it's located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Set up the server
    handler = MyHandler
    with ReusableTCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Tole.ge local server is running!")
        print(f"🔗 Open your browser and go to: http://localhost:{PORT}")
        print("🛑 Press Ctrl+C in the terminal to stop the server.")

        # Automatically open the site in your default browser
        webbrowser.open(f"http://localhost:{PORT}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped successfully.")


if __name__ == "__main__":
    run_server()