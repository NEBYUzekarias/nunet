from db import Credential, Service, Device 
from db.interface import Database   

import logging
log = logging.getLogger("session_manager_admin")

db = None

def set_db(db_file, db_create=False, logger=None):
    global db
    db = Database(db_file, db_create, logger)


def add_credential(username, password):
    if db.add(Credential, username=username, password=db.hash_password(password)):
        log.info("Credential with username '{}' added.".format(username))
    else:
        log.error("Error adding '{}'!".format(username))

username = "nebyu"
password = "26535986"

db_file = "session.db"

set_db(db_file, False , log )
add_credential(username, password)