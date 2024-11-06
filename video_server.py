import cv2, imutils, socket
import numpy as np
import time
import base64
import threading, wave,pickle,struct
import sys
import queue
import os

BUFF_SIZE = 65536
host_ip = '127.0.0.1'
port = 8000
socket_address = (host_ip,port)

# memulai server
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
server_socket.bind(socket_address)
print('Listening at :',socket_address)

def video_stream():
    while (True):
        # ambil data
        msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
        # dekode pesan yang didapat
        data = base64.b64decode(msg)
        # konversikan data yang sudah didekode
        npdata = np.fromstring(data,dtype=np.uint8)
        # dekode data menjadi gambar
        frame = cv2.imdecode(npdata,1)
        # tampikan gambar untuk debug
        cv2.imshow("RECEIVING VIDEO", frame)
        if cv2.waitKey(1) == ord('q'):
            break
             
# video_stream()
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
	executor.submit(video_stream)