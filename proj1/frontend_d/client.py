import pickle
import socket
from datetime import datetime
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user=""
pswd=""
request=0
def start_connection():
    port=12345
    host_ip=socket.gethostbyname(socket.gethostname())
    host_ip="172.16.180.123"
    s.connect((host_ip,port))

def signup_req():
    sign_packet=[request,user,pswd]
    s.send(pickle.dumps(sign_packet))

# start_connection()
# signup_req()
# s.connect((socket.gethostbyname(socket.gethostname()),port))
