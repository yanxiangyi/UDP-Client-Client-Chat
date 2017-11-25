# Import socket module
from socket import *
# Import threading module
import threading


# Method used to receive message and exit chat
def receive(clientSocket):
    global flag
    while flag:
        message = clientSocket.recv(1024).decode("utf-8")
        # Enter !exit to leave
        if message == "!exit":
            flag = False
        print(message)


print('Please input your name: ')
# Assign a port number
serverPort = 12000
# Create a UDP client socket
#  (AF_INET is used for IPv4 protocols)
#  (SOCK_DGRAM) is used for UDP
clientSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to local server address and server port
clientSocket.connect(("127.0.0.1", serverPort))
# Set a flag ready to exit
flag = True
# Use multi-threading methods to receive messages
trd = threading.Thread(target=receive, args=(clientSocket,))
# Start multi-threading
trd.start()
userid = input()
clientSocket.send(userid.encode('utf-8'))
while flag:
    message = input()
    # Send messages to server
    clientSocket.send((userid + ': ' + message).encode('utf-8'))
    if message == "exit":
        flag = False
clientSocket.close()
