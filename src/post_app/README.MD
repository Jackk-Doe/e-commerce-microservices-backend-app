# Compile Proto-Buffer file with this command
`$ python -m grpc_tools.protoc -I ../../protos/ --python_out=. --grpc_python_out=. ../../protos/product.proto`

NOTE : python package `grpc_tools` is required.<br><br>

# Run with
`$ python main.py`