
import socket
import threading
import time


def handle_client(connection, address):
    start_time = time.time()

    print(f"Client {address} connected!")
    print("Waiting for message...")

    time.sleep(10)

    data = connection.recv(1024)
    message = data.decode()

    print("Client says:", message)

    connection.sendall("Hello from Thread Server!".encode())

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Client {address} finished in {elapsed:.2f} seconds")

    connection.close()


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("127.0.0.1", 5000))
server.listen()

print("Thread-based server is running...")

while True:
    connection, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(connection, address)
    )

    thread.start()
