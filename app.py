from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps


class RequestDumper(BaseHTTPRequestHandler):
    def do_GET(self):
        self.generate_response()

    def do_POST(self):
        self.generate_response()

    def do_PUT(self):
        self.generate_response()

    def do_PATCH(self):
        self.generate_response()

    def do_DELETE(self):
        self.generate_response()

    def generate_response(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(
            bytes(f"{dumps(self.generate_output(), indent=4)}\n", "utf8")
        )

    def generate_output(self):
        return {
            "client": self.client_address[0],
            "method": self.command,
            "path": self.path,
            "headers": {item[0]: item[1] for item in self.headers.items()},
        }


server = HTTPServer(("0.0.0.0", 8080), RequestDumper)

if __name__ == "__main__":
    try:
        server.serve_forever()
    except:
        server.server_close()
