import asyncio
import time
import math

async def send_request(host, port):
    start_time = time.perf_counter()

    reader, writer = await asyncio.open_connection(host, port)

    request = (
        b"GET / HTTP/1.1\r\n"
        b"Host: 127.0.0.1\r\n"
        b"Connection: close\r\n"
        b"\r\n"
    )

    writer.write(request)
    await writer.drain()

    response = await reader.read()

    end_time = time.perf_counter()

    latency = end_time - start_time

    writer.close()
    await writer.wait_closed()

    return latency


async def run_benchmark(host, port, num_clients):

    start_time = time.perf_counter()

    tasks = [
        send_request(host, port)
        for _ in range(num_clients)
    ]

    latencies = await asyncio.gather(*tasks)

    end_time = time.perf_counter()

    total_time = end_time - start_time
    throughput = num_clients / total_time

    print("Number of clients:", num_clients)
    print("Total time:", total_time)
    print("Latencies:", latencies)
    print("Throughput:", throughput, "requests/second")
    p50 = percentile(latencies, 0.50)
    p95 = percentile(latencies, 0.95)
    p99 = percentile(latencies, 0.99)

    print("p50:", p50 * 1000, "ms")
    print("p95:", p95 * 1000, "ms")
    print("p99:", p99 * 1000, "ms")

def percentile(data, p):
    sorted_data = sorted(data)
    index = math.ceil(p * len(sorted_data)) - 1
    return sorted_data[index]


async def main():
    await run_benchmark("127.0.0.1", 5000, 10)

asyncio.run(main())