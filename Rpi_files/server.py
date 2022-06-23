import socket
import os

HOST = str(os.system('hostname -I'))

print(HOST)
PORT = 17171

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


try:
    while True:
        server.listen(5)
        communication_socket, address = server.accept()
        print(f"Connected to {address}")
        while 1:
            #wait here
            message = communication_socket.recv(4096)
            if not message: break
            communication_socket.send(f"Message recieved! Thank you!".encode('UTF-8'))
            file1 = open('ins.txt', 'w')
            print(str(message))
            file1.write(str(eval(message)))
            file1.close()
        #disconnect when main.py or other file is done running
        communication_socket.close()
        print(f"Connection with {address} ended!")
except:
    print("server stopped")
