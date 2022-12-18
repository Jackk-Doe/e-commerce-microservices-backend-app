# Proto generate with this command
`$ python -m grpc_tools.protoc -I ../../protos/ --python_out=. --grpc_python_out=. ../../protos/product.proto`

# Run with
`$ python main.py`