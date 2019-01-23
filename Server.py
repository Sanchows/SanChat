import socket, threading, time

'''
# 24.01 00:05
the ability to view connected clients to the server
'''

'''
need to do:
 method editingClients()
 time


 cryption
 protocol
 DB
'''
class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn #socket
        self.addr = addr #list: [0] - ip , [1] - id
        threading.Thread.__init__(self)
            
    def run(self):
        isConn = False # for 
        while True:
            # if the client connects for the first time:
            if not isConn: 
                inputNameClient = self.conn.recv(1024)
                IP_CLIENT = str(self.addr[0])
                ID_CLIENT = str(self.addr[1])
                NAME_CLIENT = inputNameClient.decode("utf-8")

                print("Connected: IP[{0}] ID[{1}] N[{2}]".format(IP_CLIENT, ID_CLIENT, NAME_CLIENT))
                clients.append(self.conn)
                names_clients.append(NAME_CLIENT)
                self.conn.send("=================================\nWelcome to SanChat, bro ;3".encode())
                for client in clients:
                    if client != self.conn:
                        txtMsg = "<--- {0} joined the chat! --->".format(NAME_CLIENT)
                        client.send(txtMsg.encode())
                isConn = True
        #==== ПРИЕМ СООБЩЕНИЯ ===============================================
            replyFromClient = self.conn.recv(1024)
            INC_MESSAGE = replyFromClient.decode("utf-8")
            
            if INC_MESSAGE == '/online':
                FOR_ONLINE = '------ NOW CHATTING ------\n'
                for name in names_clients:
                    FOR_ONLINE += name + '\n'
                FOR_ONLINE += '---------------------------'
                self.conn.send(str(FOR_ONLINE).encode())
                continue
            for client in clients:
                if client != self.conn:
                    txtMsg = "{0}: {1}".format(NAME_CLIENT, INC_MESSAGE)
                    client.send(txtMsg.encode())
            
            if not replyFromClient:
                break
            print ('{0} wrote: {1}'.format(NAME_CLIENT, str(INC_MESSAGE)))
                
            if INC_MESSAGE=='/exit':
                break
        #====================================================================
        print("Disconnected: IP[{0}] ID[{1}] N[{2}]".format(IP_CLIENT, ID_CLIENT, NAME_CLIENT))
        for client in clients:
            if client != self.conn:
                txtMsg = "\n<--- {0} has exit the chat --->".format(NAME_CLIENT)
                client.send(txtMsg.encode())

        clients.remove(self.conn)
        names_clients.remove(NAME_CLIENT)         
        self.conn.close()
#==============================================================================================================
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 9088))
conn.listen(5)

clients = []
names_clients = []

while True: 
    connS, addr = conn.accept()
    ClientThread(connS, addr).start()