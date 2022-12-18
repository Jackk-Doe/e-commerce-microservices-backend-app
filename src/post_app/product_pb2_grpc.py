# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import product_pb2 as product__pb2


class ProductStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProducts = channel.unary_stream(
                '/product.Product/GetProducts',
                request_serializer=product__pb2.Null.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.GetProductById = channel.unary_unary(
                '/product.Product/GetProductById',
                request_serializer=product__pb2.Id.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.CreateProduct = channel.unary_unary(
                '/product.Product/CreateProduct',
                request_serializer=product__pb2.ProductFormRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.UpdateProduct = channel.unary_unary(
                '/product.Product/UpdateProduct',
                request_serializer=product__pb2.ProductUpdateFormRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.DeleteProduct = channel.unary_unary(
                '/product.Product/DeleteProduct',
                request_serializer=product__pb2.Id.SerializeToString,
                response_deserializer=product__pb2.Status.FromString,
                )


class ProductServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProducts': grpc.unary_stream_rpc_method_handler(
                    servicer.GetProducts,
                    request_deserializer=product__pb2.Null.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'GetProductById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductById,
                    request_deserializer=product__pb2.Id.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=product__pb2.ProductFormRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=product__pb2.ProductUpdateFormRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'DeleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProduct,
                    request_deserializer=product__pb2.Id.FromString,
                    response_serializer=product__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.Product', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Product(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/product.Product/GetProducts',
            product__pb2.Null.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/GetProductById',
            product__pb2.Id.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/CreateProduct',
            product__pb2.ProductFormRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/UpdateProduct',
            product__pb2.ProductUpdateFormRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/DeleteProduct',
            product__pb2.Id.SerializeToString,
            product__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
