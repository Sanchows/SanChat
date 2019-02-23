import socket
from modules.clientprocessing.streams import *

def start_session(sock):
    try:
        inputStream = InputClientStream(sock)
        outputStream = OutputClientStream(sock)

        registration_client(sock)
    except:
        print ("Error!\nRegistration is interrupted by user!")
        sock.close()
        os._exit(1)
    else:
        try:
            outputStream.start()
            inputStream.start()
        except:
            sock.close()

def registration_client(sock):
    print ('You are connected to server. Enter your name: ', end='')
    while True:
        nick_name = str(input("Please, enter your name: "))
        if nick_name.isspace() or not nick_name.isalnum():
            print ("Valid characters are: A-z,А-я,0-9.\nPlease, enter your name: ", end='')
            continue
        sock.send(nick_name.encode())  
        break