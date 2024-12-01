import socket
import cv2
import base64
import time
import threading

class video_sender:
    def __init__(self,video_id,server_ip,server_port):
        self.debug = False
        self.video_res = (640,480)
        self.buffer_size = 655360
        self.video_id = video_id
        self.server = (server_ip,server_port)
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,self.buffer_size)
        self.daemon = True
        self.run = True
        self.token = ""
        pass
    
    def set_token(self, token):
        self.token = token

    def start(self):
        self.thread = threading.Thread(target=self.video_stream)
        self.thread.daemon = self.daemon
        self.thread.run()

    def send_data(self,data=""):
        message = base64.b64encode(data.encode('utf-8'))
        token = bytes(self.token,'utf-8')
        message = b'2'+token+message
        self.socket.sendto(message, self.server)
        
    def video_stream(self):
        while True:
            if self.run:
                cap = cv2.VideoCapture(self.video_id)
                print("Streaming to ",self.server)
                
                while cap.isOpened() and self.run:
                    # ambil frame
                    ret, frame = cap.read()
                    # persiapkan video untuk dikirim
                    frame = cv2.resize(frame,self.video_res)
                    encoded, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
                    # rubah frame gambar menjadi base64
                    message = base64.b64encode(buffer)
                    # kirim frame gambar
                    token = bytes(self.token, 'utf-8')
                    message = b'1'+token+message

                    self.socket.sendto(message,self.server)
                    # untuk debug
                    if self.debug:
                        cv2.imshow("Video transmited", frame)
                        if cv2.waitKey(1) == ord('q'):
                            break
                cap.release()
            else:
                time.sleep(0.5)