import socket
import threading
import os
'''
Added handler event, when is impossible connecting to server
Added handler for sudden closing of program (50%)
'''
class otherClients(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                replyFromOtherClients = sock.recv(1024) 
                print ('\n'+str(replyFromOtherClients.decode('utf-8')))
            except:
                sock.close()
                break
        os._exit(1)

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                textMsg = str(input(clientName+': '))
                sock.send(textMsg.encode())
                if textMsg == '/exit':
                    break
            except:
                sock.close()
                break
        os._exit(1)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9092))
except:
    print('Error connecting to server')
    os._exit(1)
print ('You are connected to server. Enter your name: ', end='')
clientName = input()

sock.send(clientName.encode())  

Client().start()
otherClients().start()