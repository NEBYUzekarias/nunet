from __future__ import print_function
import logging

import grpc

import session_pb2_grpc as sm_pb2_grpc
import session_pb2 as sm_pb2



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = sm_pb2_grpc.SessionManagerStub(channel)
        # response = stub.SignUP(sm_pb2.SignupInput(username='nebyu zakarias zewde',
        #                                         password=u'26535986',
        #                                         device_name = 'samsung'        ))

<<<<<<< HEAD
        response = stub.Login(sm_pb2.LoginInput(username='nebyu zakarias zewde',
                                                password=u'26535986',
                                                device_name = 'samsung'   ))

        # response = stub.Logout(sm_pb2.LogoutInput(device_name = 'sam'   ))
        
        print("Greeter client received: " + str(response.status))
=======
        # response = stub.Login(sm_pb2.LoginInput(username='nebyu zakarias zewde',
        #                                         password=u'26535986',
        #                                         device_name = 'samsung'   ))

        r,_ = stub.Logout.with_call(sm_pb2.LogoutInput(device_name = 'samsung'   ) , metadata=(("access_token", "MNVQEZA0AJIMUTKm"),))
        
        print("Greeter client received: " + str(r.status) )
>>>>>>> 96c580dcb754ad5836754600bfc49c72d44aadd4


if __name__ == '__main__':
    logging.basicConfig()
    run()
