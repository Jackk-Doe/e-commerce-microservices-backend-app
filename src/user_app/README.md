# Compile Proto-Buffer file with this command
From this (user_app) folder, type :
`$ python -m grpc_tools.protoc -I ../../protos/ --python_out=. --grpc_python_out=. ../../protos/user.proto`

NOTE : python package `grpc_tools` is required.<br><br>

# Run with
`$ python main.py`