import socket

def online(list_names_clients, socket):
    tmpStr = '------ NOW CHATTING ------\n'
    for name in list_names_clients:
        tmpStr += name + '\n'
    tmpStr += '---------------------------'
    
    socket.send(str(tmpStr).encode())