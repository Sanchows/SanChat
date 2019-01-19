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
                data = conn.recv(1024)
                isConn = True
                print(data.decode("utf-8"))
            
            replyFromClient = conn.recv(1024)
            
            if not replyFromClient:
                break
            
            print (str(data.decode("utf-8")) + ' пишет: ' + str(replyFromClient.decode("utf-8")))
            
            if replyFromClient.decode('utf-8')=='/exit':
                break         
            conn.send(replyFromClient.decode("utf-8").upper().encode())
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9090))
server.listen(5)

while True:
    conn, addr = server.accept()
    ClientThread(conn, addr).start()