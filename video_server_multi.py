import cv2, imutils, socket
import numpy as np
import time
import base64
import threading, wave,pickle,struct
import sys
import queue
import os
import redis
import mysql.connector


BUFF_SIZE = 65536
host_ip = '127.0.0.1'
port = 8000
socket_address = (host_ip,port)
client_addr = []


store = redis.Redis(host='localhost', port=6379, decode_responses=True)
mysql_server = mysql.connector.connect(
  host="127.0.0.1",
  user="app",
  password="password",
  database="vid"
)


class device_addr:
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
        cursor.execute("SELECT * FROM `dev_addr`")
        self.dev_addr = cursor.fetchall()
        cursor.close()
        print("Dev addr loaded")
        pass

    def check_address(self,dev_addr):
        # mysql_cursor = mysql_server.cursor(buffered=True)
        # mysql_cursor.execute("SELECT * FROM `dev_addr` WHERE `dev_addr` LIKE %s",(dev_addr,))
        # row_count = mysql_cursor.rowcount
        # mysql_cursor.close()
        # sts = True
        for id, addr in self.dev_addr:
            if addr == dev_addr:
                return True
        # if(row_count == 0):
        sql = "INSERT INTO dev_addr (dev_addr) VALUES (%s)"
        val = (dev_addr,)
        insert_cursor = self.server.cursor()
        insert_cursor.execute(sql,val)
        self.server.commit()
        print("Recorded address ",dev_addr)
        insert_cursor.close()
        self.load_dev_addr()
        return True
        # else:
        #     # print(dev_addr)
        #     return False

dev_addr = device_addr('localhost','app','password','vid')
# memulai server
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
server_socket.bind(socket_address)
print('Listening at :',socket_address)

def video_stream():
    while (True):
        # ambil data
        msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
        address = client_addr[0]
        status = dev_addr.check_address(address)
        # print(type(msg))
        # decoded = base64.b64decode(msg)
        # data = np.fromstring(decoded,dtype=np.uint8)
        if status:
            store.set(address,msg)
        # print("frame from ",address)
        # time.sleep(1)


def show_video():
    cursor = mysql_server.cursor(buffered=True)
    sql = "SELECT * FROM dev_addr"
    cursor.execute(sql)
    result = cursor.fetchall()
    while True:
        for (id,addr) in result :
            data = store.get(addr)
            # print(addr)
            # print(data)
            if data :
                print("valid frame from ",addr)
                decoded = base64.b64decode(data)
                npdata = np.frombuffer(decoded, dtype=np.uint8)
                frame = cv2.imdecode(npdata,1)
                title = "RECEIVING FROM "+addr
                cv2.imshow(title, frame)
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                print("No frame data from ",addr)
            # # decoded = np.frombuffer(msg, np.uint8)
            # # dekode pesan yang didapat
            # decoded = base64.b64decode(data)
            # # konversikan data yang sudah didekode
            # npdata = np.fromstring(decoded,dtype=np.uint8)
            # # dekode data menjadi gambar
            # frame = cv2.imdecode(npdata,1)
            # # frame =  cv2.imdecode(data, 1)
            # # tampikan gambar untuk debug
            # title = "Video from "+addr
            # cv2.imshow("RECEIVING VIDEO", frame)
            # if cv2.waitKey(1) == ord('q'):
            #     break
            # time.sleep(0.5)
             
# video_stream()
# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=2) as executor:
# 	executor.submit(video_stream)
#     executor.submit(show_video)
thread_stream = threading.Thread(target=video_stream)
thread_stream.daemon=True
thread_stream.start()
show_video()