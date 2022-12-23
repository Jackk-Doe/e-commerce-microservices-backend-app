import grpc
import logging

import envs as _envs
import database.db as _db
import services.product as _services_product
import services.inventory as _services_inventory
from product_pb2 import Id, Status, ProductInputForm, ProductIdWithUserId, ProductUpdateInputForm, ProductDTO
from product_pb2_grpc import ProductServicer, add_ProductServicer_to_server


logger = logging.getLogger(__name__)

# TODO : Fix database closing, may need to close manually
# This function to access database
def get_db():
    db = _db.SessionLocal()
    try:
        yield db
        print("DB Closing")
        db.close()
    except Exception as err:
        logger.error(str(err))


class Product(ProductServicer):
    async def GetProducts(self, request, context):
        db_gen = get_db()
        db = next(db_gen)
        # TODO : Put in try-except
        for product in await _services_product.get_products(db=db):
            inventory = await _services_inventory.get_inventory_by_product_id(db=db, p_id=product.id)
            # TODO : Get product image
            if not inventory:
                await context.abort(grpc.StatusCode.NOT_FOUND, "Product of the given request ID has no Inventory")
            product_dto = product.toProductDTO(amount=inventory.amount)
            yield product_dto
        db.close()


    async def GetProductById(self, request, context):
        if request.value == "":
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request Product ID can't be EMPTY")

        db_gen = get_db()
        db = next(db_gen)
        try:
            product = await _services_product.get_product_by_id(db=db, id=request.value)
        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))

        if not product:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Product of the given request ID is not found")

        # TODO : Get product image

        # Get Inventory amount of the [product]
        try:
            inventory = await _services_inventory.get_inventory_by_product_id(db=db, p_id=product.id)
        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))

        if not inventory:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Product of the given request ID has no Inventory")

        product_dto = product.toProductDTO(amount=inventory.amount)

        db.close()
        return product_dto


    async def CreateProduct(self, request, context):
        db_gen = get_db()
        db = next(db_gen)

        try:
            # Create to Product database
            created_product = await _services_product.create_product(
                db=db,
                name=request.name,
                des=request.description,
                seller_id=request.seller_id,
                price=request.price
            )

            # Create Inventory into database
            new_inventory = await _services_inventory.create_inventory(
                db=db,
                p_id=created_product.id,
                amount=request.amount
            )

        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))

        # TODO LATER : Upload product image after storing in DB
        
        product = created_product.toProductDTO(amount=new_inventory.amount)
        
        db.close()
        return product


    async def DeleteProduct(self, request, context):
        if request.product_id.value == '' or request.user_id.value == '':
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request Product ID and User ID can't be EMPTY")

        status = Status() #Default: False

        db_gen = get_db()
        db = next(db_gen)

        try:
            product = await _services_product.get_product_by_id(db=db, id=request.product_id.value)
        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))

        if not product:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Deleting product of the given request ID is not found")

        if product.seller_id != request.user_id.value:
            await context.abort(grpc.StatusCode.PERMISSION_DENIED, "Requesting User is not an owner of this Product")

        # TODO : Delete image

        try:
            await _services_product.delete_product(db=db, product_id=request.product_id.value)
            await _services_inventory.delete_inventory_by_product_id(db=db, p_id=request.product_id.value)
            status.value = True #Delete Success
        except Exception as err:
            logger.error("Exception with: %s", str(err))

        db.close()
        return status


    async def UpdateProduct(self, request, context):
        if request.ids.product_id.value == '' or request.ids.user_id.value == '':
            await context.abort(grpc.StatusCode.NOT_FOUND, "Request Product ID and User ID can't be EMPTY")
        db_gen = get_db()
        db = next(db_gen)

        try:
            product = await _services_product.get_product_by_id(db=db, id=request.ids.product_id.value)
        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))
        if not product:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Product of the given request ID is not found")

        if product.seller_id != request.ids.user_id.value:
            await context.abort(grpc.StatusCode.PERMISSION_DENIED, "Requesting User is not an owner of this Product")

        # TODO : Update photo

        try:
            updated_product = await _services_product.update_product(
                db=db, 
                product=product, 
                name=request.productFormRequest.name,
                des=request.productFormRequest.description,
                price=request.productFormRequest.price,
            )
            updated_inventory = await _services_inventory.update_inventory(
                db=db,
                p_id=product.id,
                amount=request.productFormRequest.amount,
            )
        except Exception as err:
            await context.abort(grpc.StatusCode.INTERNAL, str(err))

        converted_updated_product = updated_product.toProductDTO(amount=updated_inventory.amount)

        db.close()
        return converted_updated_product


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