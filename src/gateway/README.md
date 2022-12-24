# Compile Product and User Proto-Buffer files with this command
From gateway (this) folder, type :<br/>
- Product proto file with :<br/>
    `$ python -m grpc_tools.protoc -I ../../protos/ --python_out=. --grpc_python_out=. ../../protos/product.proto`

- User proto file with :<br/>
    `$ python -m grpc_tools.protoc -I ../../protos/ --python_out=. --grpc_python_out=. ../../protos/user.proto`

NOTE : python package `grpc_tools` is required.<br><br>

# Run with
`$ python main.py`