import grpc
import logging

import envs as _envs
import database.db as _db
import services.product as _services_product
from product_pb2 import Id, Status, ProductInputForm, ProductUpdateInputForm, ProductDTO
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
        product1 = ProductDTO(
            name="Test Name",
            description="Test Description",
            seller_id="This_Is_Seller_Id",
            price=99.99,
            amount=1000,
            id="This_Is_Product_Id",
            image_path="This_Is_Image_Path"
        )
        yield product1
        # return super().GetProducts(request, context)

    async def GetProductById(self, request, context):
        if request.value == "":
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request ID can't be empty")

        product1 = ProductDTO(
            name="Test Name",
            description="Test Description",
            seller_id="This_Is_Seller_Id",
            price=99.99,
            amount=1000,
            id="This_Is_Product_Id",
            image_path="This_Is_Image_Path"
        )
        return product1

    async def CreateProduct(self, request, context):
        logger.info("Input received: "+str(request))

        db_gen = get_db()
        db = next(db_gen)

        created_product = await _services_product.create_product(
            db=db,
            name=request.name,
            des=request.description,
            seller_id=request.seller_id,
            price=request.price
        )

        # TODO LATER : Upload product image after storing in DB
        # TODO : Convert to gRPC Dto
        # TODO : Update ProductDTO.amount field
        
        product = ProductDTO(
            name=created_product.name,
            description=created_product.description,
            seller_id=created_product.seller_id,
            price=created_product.price,
            amount=request.amount,
            id=created_product.id,
            image_path="This_Is_Image_Path"
        )
        logger.info("Sending: "+str(product))

        return product


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