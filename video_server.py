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

host = socket.gethostname()
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
# server_socket = socket.socket()
# server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at :',socket_address)
# server_socket.listen()
def video_stream():
    cv2.namedWindow('RECEIVING VIDEO')
    cv2.moveWindow('RECEIVING VIDEO', 10,360) 

    # conn, address = server_socket.accept()
    while True:
        msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
        print('GOT connection from ',client_addr)
        while (True):
            
            # msg = conn.recv(BUFF_SIZE).decode()
            data = base64.b64decode(msg,'/')
            
            npdata = np.fromstring(data,dtype=np.uint8)

            frame = cv2.imdecode(npdata,1)
            cv2.imshow("RECEIVING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print('quit')
                os._exit(1)
                break
             

from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=1) as executor:
	executor.submit(video_stream)