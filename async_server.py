import asyncio

import time


import asyncio
import time

async def handle_client(reader, writer):
    start_time = time.time()

    address = writer.get_extra_info("peername")
    print(f"Client {address} connected!")
    print("Waiting for message...")

    await asyncio.sleep(10)

    data = await reader.read(1024)
    message = data.decode()

    print("Client says:", message)

    writer.write("Hello from Async Server!".encode())
    await writer.drain()

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Client {address} finished in {elapsed:.2f} seconds")

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        5000
    )

    print("Async server is running...")

    async with server:
        await server.serve_forever()


asyncio.run(main())




async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        5000
    )

    print("Async server is running...")

    async with server:
        await server.serve_forever()


asyncio.run(main())