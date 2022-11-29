import pickle
import socket
from datetime import datetime
import threading

import pandas

start_time = datetime.now()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created successfully")

port=12345
# host_ip=input("Enter Server IP Address")
host_ip="172.16.180.123"

s.bind((host_ip,port))
print("socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

thread_connection={}

def store_signup(u,p):
    file=pandas.read_csv("login_details.csv")
    password=file["password"]
    username=file["username"]
    password.append(p)
    username.append(u)
    file["password"]=password
    file["username"]=username
    file.to_csv("login_details.csv",index=False)
    print("Username: ",u,"\nPassword: ",p,"\nSignedup")

def thread_connect(c,addr):
    print("Connected to",addr)
    packet=pickle.loads(c.recv(4096))
    print(packet)
    if len(packet)==3:
        if packet[0]==0:
            store_signup(packet[1],packet[2])
    

while True:
    c,addr=s.accept()
    t1 = threading.Thread(target=thread_connect, args=(c,addr))
    t1.start()




