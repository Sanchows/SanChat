import socket, threading, os

class otherClients(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True: 
            replyFromOtherClients = sock.recv(1024) 
            print (str(replyFromOtherClients.decode('utf-8')))
        

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            textMsg = str(input())
            if textMsg.isspace():
                continue
            sock.send(textMsg.strip().encode())
            if textMsg == '/exit':
                break
        
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9092))
except:
    print('Error connecting to server')
    os._exit(1)

print ('You are connected to server. Enter your name: ', end='')
while True:
    clientName = str(input())
    if clientName.isspace(): #if is empty or all symbols of string this is spaces
        print ("Please, enter your name: ", end='')
        continue
    if not clientName.isalnum():
        print ("Допустимые символы: A-z,0-9.\nPlease, enter your name: ", end='')
        continue
    sock.send(clientName.encode())  
    break

Client().start()
otherClients().start()