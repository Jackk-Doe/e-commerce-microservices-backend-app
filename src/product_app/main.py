import asyncio
import logging

import envs as _envs
import server as _server

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(levelname)s -> %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(_server.run_server())
    except KeyboardInterrupt:
        print("")
        logging.warning("CTRL+C press detected...")
        logging.warning("Shutted down Product server...")
        logging.shutdown()
    finally:
        loop.close()