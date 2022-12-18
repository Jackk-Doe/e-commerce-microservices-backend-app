import asyncio

import envs as _envs
import server as _server

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(_server.run_server())
    except KeyboardInterrupt:
        print("\nCTRL + C key detected...")
        print("Shutted down Product server...")
    finally:
        loop.close()