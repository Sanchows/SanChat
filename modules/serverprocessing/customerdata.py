
from modules.serverprocessing.handlermessage import *
import socket

def getInfo(list_addr, socket):
    NAME_CLIENT = getMessage(socket).decode("utf-8")
    info = (list_addr[0], list_addr[1], NAME_CLIENT)
    return info