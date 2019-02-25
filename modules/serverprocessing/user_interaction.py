import socket

class User():
    def __init__ (self, addr, sock):
        self.sock = sock
        self.addr = addr
    
    def get_message(self):
        try:
            message = self.sock.recv(1024)
            return (message)
        except:
            pass

    def get_userinfo(self):
        while True:
            self.NAME_CLIENT = self.get_message().decode("utf-8")
            if not self.NAME_CLIENT:
                continue
            info = (self.addr[0], self.addr[1], self.NAME_CLIENT)
            return info

    def send_to_all_other(self, list_socks, txtMsg):
        self.list_socks = list_socks
        for client in list_socks:
            if client != self.sock:
                client.send(txtMsg.encode())
    
    def to_register(self):
        self.sock.send("=================================\nWelcome to SanChat, bro ;3".encode())
        # txtMsg = "<--- {0} joined the chat! --->".format(self.NAME_CLIENT)
        # user.send_to_all_other(self.list_socks, txtMsg)  

    def disconnect(self):
        txtMsg = "\n<--- {0} has exit the chat --->".format(self.NAME_CLIENT)
        self.send_to_all_other(self.list_socks, txtMsg)    
        self.sock.close()