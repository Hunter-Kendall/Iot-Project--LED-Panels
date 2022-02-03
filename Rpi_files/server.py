import socket
import os

HOST = str(os.system('hostname -I'))

print(HOST)
PORT = 17171

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
try:
    while True:
        print("waiting")
        communication_socket, address = server.accept()
        print(f"Connected to {address}")
        message = communication_socket.recv(4096)
        print(eval(message))
        #communication_socket.send(f"Message recieved! Thank you!".encode('utf-8'))
        communication_socket.close()
        file1 = open('ins.txt', 'w')
        #print(str(message))
        file1.write(str(eval(message)))
        file1.close()
        #communication_socket.close()
        #print(f"Connection with {address} ended!")
except KeyboardInterrupt:
    print("closed")
    