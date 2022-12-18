import asyncio
import logging

import envs as _envs
import server as _server
import database.product_model as _db_product

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(levelname)s -> %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    # Connect or Create (if not existed) Product table database
    _db_product.connect_or_initialize_db()

    # Run gRPC server in Async
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