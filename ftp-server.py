#Import from the pyftpdlib module
import os
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer


#Instantiate a dummy authorizer for managing virtual users
authorizer = DummyAuthorizer()
#Define a new user having full r/w permissions and a read only
authorizer.add_user("user", "12345", "/home/rohitbadyal", perm="elradfmw")
authorizer.add_anonymous("/home/rohitbadyal", perm="elradfmw")
#Instantiate FTP handler class
handler = FTPHandler
handler.authorizer = authorizer
#Instantiate FTP server class and listen on 0.0.0.0:1026
server = FTPServer(("127.0.0.1", 1026), handler)
#Start ftp server
server.serve_forever()