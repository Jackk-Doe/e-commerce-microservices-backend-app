import grpc

import envs as _envs
from product_pb2 import Id, Status, ProductFormRequest, ProductUpdateFormRequest, ProductResponse
from product_pb2_grpc import ProductServicer, add_ProductServicer_to_server


class Product(ProductServicer):
    async def GetProducts(self, request, context):
        product1 = ProductResponse(
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

        product1 = ProductResponse(
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
        # TODO : Check duplicate in db
        # TODO : Check form [name] duplicate
        print("Input received: ", request)
        product1 = ProductResponse(
            name=request.name,
            description=request.description,
            seller_id=request.seller_id,
            price=request.price,
            amount=request.amount,
            id="This_Is_Product_Id",
            image_path="This_Is_Image_Path"
        )
        print("Sending: ", product1)
        return product1


# Function to run Server
async def run_server():
    PORT = _envs.PORT

    # Server set up
    server = grpc.aio.server()
    add_ProductServicer_to_server(Product(), server=server)
    server.add_insecure_port(f"[::]:{PORT}")

    # Start running
    await server.start()
    print("Product gRPC Asynchronous-Server is up and running...")

    await server.wait_for_termination()