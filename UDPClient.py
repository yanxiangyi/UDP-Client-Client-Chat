from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input a number: ').encode()
clientSocket.sendto(message, (serverName, serverPort))
result, serverAddress = clientSocket.recvfrom(2048)
print('Factorial from Server: ' +result.decode())
clientSocket.close()