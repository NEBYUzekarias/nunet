# nunet

nunet session manager
# comand to generate pb2 files

` python -m grpc_tools.protoc -I protos/ --python_out=. --grpc_python_out=. session.proto `