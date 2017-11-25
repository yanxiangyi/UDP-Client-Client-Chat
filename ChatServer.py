# Import socket module
from socket import *
# Import threading module
import threading


# Method used to receive message and exit chat
def receive(serverSocket):
    # The first information received is userid
    userid = sock.recv(1024).decode("utf-8")
    # Add a new user
    clients[sock] = userid
    # Initialize a user list for informing the clients
    userlist = ''
    # Server log for a user participating
    for client in clients:
        userlist = userlist + " " + clients[client]
    print('!!!FROM SERVER!!! ' + userid + ' joined chat!')
    print('!!!FROM SERVER!!! Clients now in the room:' + userlist)
    # Tell all clients the new client
    for client in clients:
        client.send(('!!!FROM SERVER!!! ' + userid + ' joined chat!').encode("utf-8"))
        client.send(('!!!FROM SERVER!!! Clients now in the room:' + userlist).encode("utf-8"))
    # Enter !exit to leave
    global flag
    while flag:
        message = serverSocket.recv(1024).decode('utf-8')
        if message == "!exit":
            flag = False
        # Send the message to all clients
        for client in clients:
            client.send(message.encode("utf-8"))
        print(message)


# Assign a port number
serverPort = 12000
# Create a UDP server socket
#  (AF_INET is used for IPv4 protocols)
#  (SOCK_DGRAM) is used for UDP
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to local server address and server port
serverSocket.bind(("127.0.0.1", serverPort))
# Listen to at most 8 connection at a time
serverSocket.listen(8)
# Initialize a new dict for clients
clients = {}
# Set a flag ready to exit
flag = True
# Server should be up and running and listening to the incoming connections
while flag:
    sock, clientAddress = serverSocket.accept()
    # Use multi-threading methods to receive messages
    trd = threading.Thread(target=receive, args=(sock,))
    # Start multi-threading
    trd.start()
    '''message = input()
    # Send messages to server
    sock.send(('Server: ' + message).encode('utf-8'))
    print('Server: ' + message)
    if message == "exit":
        flag = False'''
serverSocket.close()
