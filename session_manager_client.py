from __future__ import print_function
import logging

import grpc

import session_pb2_grpc as sm_pb2_grpc
import session_pb2 as sm_pb2



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sm_pb2_grpc.SessionManagerStub(channel)
        response = stub.Login(sm_pb2.LoginInput(username='you',
                                                password='26535986',
                                                device_name='samasug'  
        
        
        ))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
