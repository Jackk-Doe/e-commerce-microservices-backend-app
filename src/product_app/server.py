import grpc
import logging

import envs as _envs
import database.db as _db
import services.product as _services_product
from product_pb2 import Id, Status, ProductInputForm, ProductIdWithUserId, ProductUpdateInputForm, ProductDTO
from product_pb2_grpc import ProductServicer, add_ProductServicer_to_server


logger = logging.getLogger(__name__)

# This function to access database
def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Product(ProductServicer):
    async def GetProducts(self, request, context):
        db_gen = get_db()
        db = next(db_gen)
        for product in await _services_product.get_products(db=db):
            # TODO : Update amount field later
            product_dto = product.toProductDTO(amount=0)
            yield product_dto


    async def GetProductById(self, request, context):
        if request.value == "":
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request Product ID can't be EMPTY")

        db_gen = get_db()
        db = next(db_gen)
        product = await _services_product.get_product_by_id(db=db, id=request.value)
        
        if not product:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Product of the given request ID is not found")

        # TODO : Update amount field later
        product_dto = product.toProductDTO(amount=0)

        return product_dto


    async def CreateProduct(self, request, context):
        logger.info("Input received: "+str(request))
        db_gen = get_db()
        db = next(db_gen)

        # Create to Product database
        created_product = await _services_product.create_product(
            db=db,
            name=request.name,
            des=request.description,
            seller_id=request.seller_id,
            price=request.price
        )

        # TODO LATER : Upload product image after storing in DB
        # TODO : Update ProductDTO.amount field
        
        product = created_product.toProductDTO(amount=request.amount)
        logger.info("Sending: "+str(product))

        return product


    async def DeleteProduct(self, request, context):
        if request.product_id.value == '' or request.user_id.value == '':
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request Product ID and User ID can't be EMPTY")

        status = Status() #Default: False
        db_gen = get_db()
        db = next(db_gen)
        try:
            await _services_product.delete_product(db=db, product_id=request.product_id.value, user_id=request.user_id.value)
            status.value = True
        except Exception as err:
            logger.error("Exception with: %s", str(err))

        return status

# Function to run Server
async def run_server():
    PORT = _envs.PORT

    # Server set up
    server = grpc.aio.server()
    add_ProductServicer_to_server(Product(), server=server)
    server.add_insecure_port(f"[::]:{PORT}")

    # Start running
    await server.start()
    logging.info("Product gRPC Asynchronous-Server is up and running...")

    await server.wait_for_termination()