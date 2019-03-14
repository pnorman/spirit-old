#!/usr/bin/env python3
import http.server

class CachelessHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        http.server.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    http.server.test(HandlerClass=CachelessHTTPRequestHandler, port=8081, bind="127.0.0.1")
