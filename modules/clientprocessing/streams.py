import socket, threading, os

class InputClientStream(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    
    def get_message(self):
        try:
            message = self.sock.recv(1024)
            return (message)
        except:
            pass
    
    def run(self):
        while True:
            print (str(self.get_message().decode('utf-8')))

class OutputClientStream(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        while True:
            textMsg = str(input())
            if textMsg.isspace():
                continue
            self.sock.send(textMsg.strip().encode())
            
            if textMsg == '/exit':
                os._exit(1)