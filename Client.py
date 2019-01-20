import socket
import threading
import os

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
 #           print (clientName + ': ', end = '')
            try:
                textMsg = str(input(clientName+': '))
                sock.send(textMsg.encode())
                if textMsg == '/exit':
                    break
            except:
                sock.close()
                break
        os._exit(1)

clsd = False # for /exit

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

print ('You are connected to server. Enter your name: ', end='')
clientName = input()

sock.send(clientName.encode())  

Client().start()
iAmFirst = False
while True:
    if not iAmFirst:
        otherClients().start()
        iAmFirst = True