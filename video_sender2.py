import cv2, imutils, socket
import numpy as np
import time, os
import base64
import threading, wave,pickle,struct
import queue

q = queue.Queue(maxsize=15)
BUFF_SIZE = 65536

server_addr = ('127.0.0.1', 8000)
# server_addr = ''
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
# client_socket.connect(('127.0.0.1', 8000))

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    encoded, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
    message = base64.b64encode(buffer)
    client_socket.sendall(message)
    # untuk debug
    cv2.imshow("Video transmited", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=2) as executor:
#     # executor.submit(audio_stream)
#     executor.submit(get_frame)
#     executor.submit(video_stream)
# video_stream()