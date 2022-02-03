import socket
import subprocess
import sqlite3

conn = sqlite3.connect('led_lights.db')
c = conn.cursor()

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


c.execute(f"""SELECT instructions FROM Last WHERE last_light = "Last" """)
r = c.fetchone()[0]
print(r)

send(eval(r))
