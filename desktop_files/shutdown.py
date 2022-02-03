import socket
import subprocess

# setting up websocket

proc = subprocess.Popen(["ping", "csci226-hdk", "-4"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
splitw = out.split()
ip = str(splitw[2])
ip = ip.replace("b","")
ip = ip.replace("'","")
ip = ip.replace("[","")
ip = ip.replace("]","")
print(ip)

HOST = str(ip)
PORT = 5050

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

def send(ins):

    #socket.connect((HOST, PORT))
    socket.send(str(ins).encode())
    don = socket.recv(1024).decode('UTF - 8')
    print(don)


instruct = [['Static', range(0, 13), [0, 0, 0]],
            ['Static', range(13, 22), [0, 0, 0]],
            ['Static', range(22, 31), [0, 0, 0]],
            ['Static', range(31, 40), [0, 0, 0]],
            ['Static', range(40, 49), [0, 0, 0]],
            ['Static', range(49, 58), [0, 0, 0]],
            ['Static', range(58, 67), [0, 0, 0]],
            ['Static', range(67, 76), [0, 0, 0]],
            ['Static', range(76, 89), [0, 0, 0]]]


send(instruct)
