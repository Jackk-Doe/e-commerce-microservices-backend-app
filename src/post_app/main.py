import asyncio

import envs as _envs
import server as _server

if __name__ == '__main__':
    # Start a Async gRPC Server
    asyncio.run(_server.run_server())