import socket, threading, time

from modules.serverprocessing import commands
from modules.serverprocessing.user_interaction import User

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        isFirst = True
        while self.conn:
            # if the client connects for the first time:
            if isFirst: 
                user = User(self.addr, self.conn)
                IP_CLIENT, PORT, NAME_CLIENT = user.get_userinfo()
                list_socks.append(self.conn)
                list_names.append(NAME_CLIENT)
                user.to_register()
                print("Connected: IP[{0}] PORT[{1}] N[{2}]".format(IP_CLIENT, PORT, NAME_CLIENT))
                isFirst = False
            
            MESSAGE = user.get_message().decode("utf-8")
            if MESSAGE == '/online':
                commands.online(list_names, self.conn)
                continue

            txtMsg = "{0}: {1}".format(NAME_CLIENT, MESSAGE)
            user.send_to_all_other(list_socks, txtMsg)            
            if not MESSAGE:
                break
            print ('{0} wrote: {1}'.format(NAME_CLIENT, str(MESSAGE)))
                
            if MESSAGE=='/exit':
                break

        print("Disconnected: IP[{0}] PORT[{1}] N[{2}]".format(IP_CLIENT, PORT, NAME_CLIENT))
        list_socks.remove(self.conn)
        list_names.remove(NAME_CLIENT)       
        user.disconnect()  

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 9092))
conn.listen()

list_socks = []
list_names = []

while True:
    connS, addr = conn.accept()
    ClientThread(connS, addr).start()