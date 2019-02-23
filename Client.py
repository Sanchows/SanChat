import socket, threading, os

from modules.clientprocessing.init_connect import start_session

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9092))
except ConnectionRefusedError:
    print('Error connecting to server.\nCheck the data for connect to the server.')
    os._exit(1)
else:
    start_session(sock)