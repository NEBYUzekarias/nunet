 
import grpc
import sys
import os
import logging
import argparse
import random
import string

from concurrent import futures

from db import Credential, Service, Device
from db.interface import Database

sm_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, "{}/api/".format(sm_root_dir))

import session_pb2_grpc as sm_pb2_grpc
import session_pb2 as sm_pb2



logging.basicConfig(format="%(asctime)s - [%(levelname)8s] "
                           "- %(name)s - %(message)s", level=logging.INFO)
log = logging.getLogger("session_manager")

ONE_DAY_IN_SECONDS = 60 * 60 * 24


def generate_access_token(length=15):
    key = ''.join(random.choice(string.ascii_letters + string.digits)
                  for _ in range(length))
    return key.upper()


class Status:
    OK = 0
    PERMISSION_DENIED = 1
    CANCELLED = 2
    UNKNOWN = 3


class SessionManagerServicer(sm_pb2_grpc.SessionManagerServicer):

    def __init__(self, db_session, timeout=20):
        self.db = db_session
        self.timeout = timeout

    def Login(self, request, context):
        cred = self.db.query(Credential,
                             username=request.username,
                             password=request.password)
        if not cred:
            return self.set_grpc_context(
                context,
                sm_pb2.LoginOutput(status=Status.PERMISSION_DENIED,
                                   access_token=""),
                "User not registered!", grpc.StatusCode.PERMISSION_DENIED)

        # Check if the Device is already registered
        device = self.db.query(Device,
                               device_name=request.device_name,
                               username=request.username)

        # Check if the Device is the active one
        if device and cred.active_device == device.device_name:
            log.warning("Device is already active and logged in.")
            return sm_pb2.LoginOutput(status=Status.OK,
                                      access_token=device.access_token)

        access_token = generate_access_token()
        if not device:
            log.info("Registering new Device: '{}'".format(
                request.device_name))
            self.db.add(Device,
                        device_name=request.device_name,
                        access_token=access_token,
                        username=cred.username)
        elif device.access_token == "":
            log.info("Setting new access_token for: '{}'".format(
                request.device_name))
            self.db.update(Device,
                           where={"username": cred.username,
                                  "device_name": device.device_name},
                           update={"access_token": access_token})
        else:
            access_token = device.access_token
            log.warning("Device '{}' is already logged in.".format(
                request.device_name))

        # Checking if no Ghost Session was initialized yet
        if not cred.session_id:
            log.info("Calling start_session: '{}'".format(request.device_name))
            if not self.start_session(cred.username):
                return self.set_grpc_context(
                    context,
                    sm_pb2.LoginOutput(status=Status.OK,
                                       access_token=access_token),
                    "Opencog Services offline!",
                    grpc.StatusCode.OK)
        return sm_pb2.LoginOutput(status=Status.OK, access_token=access_token)

    def Logout(self, request, context):
        cred, device, access_token = self.validate_access(context)
        if not access_token:
            return self.set_grpc_context(context,
                                         sm_pb2.LogoutOutput(),
                                         "Invalid access!",
                                         grpc.StatusCode.PERMISSION_DENIED)

        if cred.active_device == request.device_name:
            log.info("The active Device is logging out...")
            self.set_active_device(device.username, "")

        log.info("Updating the Device info...")
        self.db.update(Device,
                       where={"dev_id": device.dev_id},
                       update={"access_token": ""})
        return sm_pb2.LogoutOutput(status=Status.OK)

      

class SessionManagerServer:
    def __init__(self,
                 db_file="sessions.db",
                 db_create=False,
                 port=50000):

        self.db_file = db_file
        self.db_create = db_create
        self.db = Database(db_file=db_file, db_create=db_create)
        self.port = port
        self.server = None

    def start_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
        
        sm_pb2_grpc.add_SessionManagerServicer_to_server(
            SessionManagerServicer(db_session=self.db,
                                   timeout=self.timeout), self.server)
        self.server.add_insecure_port("[::]:{}".format(self.port))
        log.info("Starting SessionManagerServer at localhost:{}".format(
            self.port))
        self.server.start()

    def stop_server(self):
        self.server.stop(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-file",
                        "-db",
                        dest="db_file",
                        default="sessions.db",
                        help="DB file name")
    parser.add_argument("--db-create",
                        action="store_true",
                        dest="db_create",
                        default=False,
                        help="Force DB creating")
    parser.add_argument("--port",
                        "-p",
                        type=int,
                        default=50000,
                        help="Session manager server port")
    
    args = parser.parse_args()

    server = SessionManagerServer(db_file=args.db_file,
                                  db_create=args.db_create,
                                  port=args.port,
                                  )
    server.start_server()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop_server()