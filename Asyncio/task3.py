# Task 3

# Echo server with asyncio

# Create a socket echo server which handles each connection using asyncio Tasks.

import asyncio

HOST = 'localhost'
PORT = 20001

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)

    print(f"Listening on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
