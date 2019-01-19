import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        isConn = False
        while True:
            if not isConn: 
                print ('Подключился клиент: ', addr, end = ' Название: ')
                data = self.conn.recv(1024)
                isConn = True
                print(data.decode("utf-8"))
            
            replyFromClient = self.conn.recv(1024)
            
            if not replyFromClient:
                break
            
            print (str(data.decode("utf-8")) + ' пишет: ' + str(replyFromClient.decode("utf-8")))
            
            if replyFromClient.decode('utf-8')=='/exit':
                break         
            self.conn.send(replyFromClient.decode("utf-8").upper().encode())
        conn.close()

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('', 9090))
conn.listen(5)

while True: 
    connS, addr = conn.accept()
    ClientThread(connS, addr).start()