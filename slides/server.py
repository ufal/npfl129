#!/usr/bin/env python3
import argparse
import http.server

class SimpleHTTPServer(http.server.ThreadingHTTPServer):
    class Handler(http.server.SimpleHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def send_header(request, header, value):
            if request.path.endswith(".svgz") and header.lower() == "content-type":
                super().send_header("Content-Type", "image/svg+xml")
                super().send_header("Content-Encoding", "gzip")
            else:
                super().send_header(header, value)

    def __init__(self, port):
        super().__init__(("", port), self.Handler)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("port", default=8000, nargs="?", type=int, help="Port")
    args = parser.parse_args()

    with SimpleHTTPServer(args.port) as server:
        try:
            host, port = server.socket.getsockname()
            print("Serving HTTP on http://{}:{}/".format(host, port))
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
