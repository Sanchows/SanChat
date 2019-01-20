import socket
import threading
import time

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        isConn = False
        while True:
            if not isConn: # if the client connects for the first time
                data = self.conn.recv(1024)
                print ('Connected: ' + 'IP ['+ str(self.addr[0]) + '] ID[' + str(self.addr[1]) + '] N['+ data.decode('utf-8') + ']')
                isConn = True
                clients.append(self.conn)
            
            replyFromClient = self.conn.recv(1024)

            for client in clients:
                if client != self.conn:
                    txtMsg = data.decode('utf-8') + ': ' + replyFromClient.decode('utf-8') 
                    client.send(txtMsg.encode())
            
            if not replyFromClient:
                break
            print (str(data.decode("utf-8")) + ' wrote: ' + str(replyFromClient.decode("utf-8")))
                
            if replyFromClient.decode('utf-8')=='/exit':
                print ('Disconnected: ' + 'IP ['+ str(self.addr[0]) + '] ID[' + str(self.addr[1]) + '] N['+ data.decode('utf-8') + ']')
                clients.remove(self.conn)
                break         
        self.conn.close()

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 9090))
conn.listen(5)

clients = []
con_list = []

while True: 
    connS, addr = conn.accept()
    ClientThread(connS, addr).start()