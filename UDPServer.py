from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('127.0.0.1', serverPort))

print('The server is ready to receive')

def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n-1)

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message.decode())
    if int(message.decode()) < 0:
        result = 'Factorial not defined for negative values.'
    elif int(message.decode()) >= 0:
        result = str(factorial(int(message.decode())))
    serverSocket.sendto(result.encode(), clientAddress)