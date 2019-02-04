import socket

def getMessage(socket):
    message = socket.recv(1024)
    return (message)