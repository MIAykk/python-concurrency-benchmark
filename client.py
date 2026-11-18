import socket

# 1. Create a socket
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# 2. Connect to the server
client.connect(("127.0.0.1", 5000))

print("Connected to server!")

# 3. Send a message
client.sendall("Hello from Client!".encode())

# 4. Receive server response
response = client.recv(1024)

print("Server says:", response.decode())

# 5. Close connection
client.close()