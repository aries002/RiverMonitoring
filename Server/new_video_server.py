import cv2
import socket
import redis
import mysql.connector
import threading
import base64
import json

class device_auth:
    def __init__(self,host,user,password,database):
        self.server = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.load_dev_addr()

    def load_dev_addr(self):
        cursor = self.server.cursor(buffered=True)
        # eksekusi pengambilan token
        cursor.execute("SELECT token, dev_id FROM `dev_auth`")
        # simpan hasil pencarian token
        self.dev_auth = cursor.fetchall()
        print(self.dev_auth)
        cursor.close()
        print("Dev addr loaded")
        pass

    def check_address(self,dev_token):
        # print(dev_token)
        for token, addr in self.dev_auth:
            if token == dev_token:
                return addr
        return False
   

dev_addr = device_auth('localhost','app','password','water_level')
store = redis.Redis(host='localhost', port=6379, decode_responses=True)
# memulai server
BUFF_SIZE = 655360
host_ip = '0.0.0.0'
port = 8000
socket_address = (host_ip,port)
debug = True
def video_stream():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
    server_socket.bind(socket_address)
    print('Listening at :',socket_address)
    while (True):
        # ambil data
        msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
        kode = msg[0:1]
        token = msg[1:65]
        token = token.decode("utf-8")
        address = dev_addr.check_address(token)

        # status = dev_addr.check_address(address)
        if address != False:
            data = msg[65:]
            # print(img)
            if(kode == b'1'):
                store.set(address,data)
            if(kode == b'2'):
                decoded = base64.b64decode(data)
                address = address+"_data"
                store.set(address,decoded)

video_stream()