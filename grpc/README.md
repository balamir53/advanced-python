## Setup
> git clone -b v1.50.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc  
> cd grpc/examples/python/route_guide  
> python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/route_guide.proto  

