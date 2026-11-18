import socket

# 1. Create a socket
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# 2. Choose IP and Port
server.bind(("127.0.0.1", 5000))

# 3. Start listening
server.listen()

print("Server is waiting for a client...")

# 4. Accept a client connection
connection, address = server.accept()

print("Connected by:", address)

# 5. Receive message
message = connection.recv(1024)

print("Client says:", message.decode())

# 6. Send response
connection.sendall("Hello from Server!".encode())

# 7. Close connection
connection.close()
server.close()