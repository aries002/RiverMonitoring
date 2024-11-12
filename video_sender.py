import cv2, imutils, socket
import numpy as np
import base64
import threading


class video_sender:
    def __init__(self,video_id,server_ip,server_port):
        self.debug = False
        self.video_res = (640,480)
        self.buffer_size = 65536
        self.video_id = video_id
        self.server = (server_ip,server_port)
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,self.buffer_size)
        self.daemon = True
        pass
    
    def start(self):
        self.thread = threading.Thread(target=self.video_stream)
        self.thread.daemon = self.daemon
        self.thread.run()

    def video_stream(self):
        cap = cv2.VideoCapture(self.video_id)
        print("Streaming to ",self.server)
        
        while cap.isOpened():
            # ambil frame
            ret, frame = cap.read()
            # persiapkan video untuk dikirim
            frame = cv2.resize(frame,self.video_res)
            encoded, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
            # rubah frame gambar menjadi base64
            message = base64.b64encode(buffer)
            # kirim frame gambar
            self.socket.sendto(message,self.server)
            # untuk debug
            if self.debug:
                cv2.imshow("Video transmited", frame)
                if cv2.waitKey(1) == ord('q'):
                    break

# streamer = video_sender(0,'localhost',8000)
# streamer.video_stream()
# video_stream()