import socketserver
import time
class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("Client connected:", self.client_address)
        request_data = b""

        while b"\r\n\r\n" not in request_data:
            chunk = self.request.recv(4096)

            if not chunk:
                return

            request_data += chunk
        request_line = request_data.split(b"\r\n", 1)[0]

        print("HTTP Request:", request_line.decode())   

        body = b"Hello from Thread-Based HTTP Server!"

        response = (
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain\r\n"
            + f"Content-Length: {len(body)}\r\n".encode()
            + b"Connection: close\r\n"
            + b"\r\n"
            + body
        )
        self.request.sendall(response)
        print("HTTP Response sent!")
        self.request.close()
class ThreadedHTTPServer(socketserver.ThreadingTCPServer):
    
    allow_reuse_address = True
    daemon_threads = True
    request_queue_size = 100


server = ThreadedHTTPServer(
    ("127.0.0.1", 5000),
    RequestHandler
)

print("Thread-Based HTTP Server is running...")

server.serve_forever()