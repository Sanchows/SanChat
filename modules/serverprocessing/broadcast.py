import socket

def toAllOther(list_clients, socket, txtMsg):
    for client in list_clients:
        if client != socket:
            client.send(txtMsg.encode())
