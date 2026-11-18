import asyncio
async def handle_client(reader, writer):
    print("Client connected!")

    request_data = await reader.readuntil(b"\r\n\r\n")
    request_line = request_data.split(b"\r\n", 1)[0]

    print("HTTP Request:", request_line.decode())
    body = b"Hello from Asyncio HTTP Server!"

    response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/plain\r\n"
        + f"Content-Length: {len(body)}\r\n".encode()
        + b"Connection: close\r\n"
        + b"\r\n"
        + body
    )

    writer.write(response)
    await writer.drain()

    print("HTTP Response sent!")

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        5000,
        backlog=100
    )

    print("Asyncio HTTP Server is running...")

    async with server:
        await server.serve_forever()


asyncio.run(main())