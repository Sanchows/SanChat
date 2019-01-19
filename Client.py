import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

print ('You are connected to server. Enter your name: ', end='')
clientName = input()
sock.send(clientName.encode())
while True:
    print (clientName + ': ', end = '')
    textMsg = str(input())
    sock.send(textMsg.encode())
    replyFromServer = sock.recv(1024)
    if textMsg == '/exit':
        break
    print('Server: ' + str(replyFromServer.decode("utf-8")))


sock.close()