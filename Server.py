import socket, threading, time

from modules.serverprocessing import broadcast
from modules.serverprocessing import commands
from modules.serverprocessing import customerdata

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn #socket
        self.addr = addr #list: [0] - ip , [1] - id
        threading.Thread.__init__(self)
                
    def run(self):
        isFirst = True # for first client connection
        while self.conn:
            # if the client connects for the first time:
            if isFirst: 
                
                IP_CLIENT, ID_CLIENT, NAME_CLIENT = customerdata.getInfo(self.addr, self.conn)
                
                clients.append(self.conn)
                names_clients.append(NAME_CLIENT)

                print("Connected: IP[{0}] ID[{1}] N[{2}]".format(IP_CLIENT, ID_CLIENT, NAME_CLIENT))
                
                self.conn.send("=================================\nWelcome to SanChat, bro ;3".encode())
                
                txtMsg = "<--- {0} joined the chat! --->".format(NAME_CLIENT)
                broadcast.toAllOther(clients, self.conn, txtMsg)

                isFirst = False
                                
#==== ПРИЕМ СООБЩЕНИЯ  
            replyFromClient = self.conn.recv(1024)
            INC_MESSAGE = replyFromClient.decode("utf-8")
            
            if INC_MESSAGE == '/online':
                commands.online(names_clients, self.conn)
                continue

            txtMsg = "{0}: {1}".format(NAME_CLIENT, INC_MESSAGE)
            broadcast.toAllOther(clients, self.conn, txtMsg)
            
            if not replyFromClient:
                break
            print ('{0} wrote: {1}'.format(NAME_CLIENT, str(INC_MESSAGE)))
                
            if INC_MESSAGE=='/exit':
                break

#==== IF DISCONNECT (self.conn = false)
        print("Disconnected: IP[{0}] ID[{1}] N[{2}]".format(IP_CLIENT, ID_CLIENT, NAME_CLIENT))
        
        txtMsg = "\n<--- {0} has exit the chat --->".format(NAME_CLIENT)
        broadcast.toAllOther(clients, self.conn, txtMsg)

        clients.remove(self.conn)
        names_clients.remove(NAME_CLIENT)         
        
        self.conn.close()
#=========================================
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 9092))
conn.listen()

clients = []
names_clients = []

while True:
    connS, addr = conn.accept()
    ClientThread(connS, addr).start()