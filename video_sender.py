import cv2, imutils, socket
import numpy as np
import time, os
import base64
import threading, wave,pickle,struct
import queue

BUFF_SIZE = 65536
server_addr = ('127.0.0.1', 8000)

# persiapan socker UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
#capture video
cap = cv2.VideoCapture(0)

def video_stream():
    while True:
        # ambil frame
        ret, frame = cap.read()
        # persiapkan video untuk dikirim
        encoded, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
        # rubah frame gambar menjadi base64
        message = base64.b64encode(buffer)
        # kirim frame gambar
        client_socket.sendto(message,server_addr)
        # untuk debug
        cv2.imshow("Video transmited", frame)
        if cv2.waitKey(1) == ord('q'):
            break

# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=2) as executor:
#     # executor.submit(audio_stream)
#     executor.submit(get_frame)
#     executor.submit(video_stream)
video_stream()