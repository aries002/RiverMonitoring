import os
import configparser
import requests
import cv2, imutils
import socket
import numpy as np
import base64
import threading
import time
DEF_LOCATION = ""
DEF_TEMPLATE = './config_template.conf'


class config:
    def __init__(self, config_location = ''):
        self.def_if = 'testing'
        self.config_location =config_location
        if config_location == '':
            config_location = DEF_LOCATION
        if not os.path.isfile(config_location):
            self.create_conf()
        self._config = configparser.ConfigParser()
        self._config.read(config_location)
        self.debug = False
    
    # buat file konfigurasi
    def create(self):
        new_config = configparser.ConfigParser()
        if not os.path.isfile(DEF_TEMPLATE):
            print("Template not found exiting")
        else:
            new_config.read(DEF_TEMPLATE)
            with open(self.config_location, 'w') as configfile:
                new_config.write(configfile)
                configfile.close()

    # simpan konfigurasi
    def save(self):
        pass

    # print konfigurasi
    def print(self):
        #  data in self.data:?
        for section in self._config.sections():
            print('[',section,']')
            for config in self._config[section]:
                print(config, "=", self._config[section][config],'(',type(self._config[section][config]),')')
        # print(self._config.sections())
    

class api_client:
    def __init__(self,url):
        self.url = url
        self.uri = {
            'image' : '',
            'status' : 'status',
            'sensor_data' : '',
            'recent_image' : ''
        }
        self.header ={}
        self.debug = False
        pass

    def get_status(self):
        url = self.url+self.uri['status']
        header = self.header

        result = requests.get(url, headers=header)
        return result.text
    
    def send_sensor(self,data):
        url = self.url+self.uri['sensor_data']

        result = requests.post(url, headers=self.header, json=data)
        
        return result
    
    def send_image(self,base64_img, url = None):
        if url is None:
            url = self.url+self.uri['image']

        result = requests.post(url,headers=self.header,data=base64_img)

        return result
    
    def send_recent_video_img(self,vid_id, file_name = "file", url = None):
        if url is None:
            url = self.url+self.uri['recent_image']
        
        cap = cv2.VideoCapture(vid_id)
        if cap.isOpened():
            res, image = cap.read()
            if image is None:
                return False
        else:
            return False
        file = {file_name:image}
        
        result = requests.post(url, headers=self.header, files=file)

        return result


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

    def send_data(self,data="", data_type = b'2'):
        message = base64.b64encode(data.encode('utf-8'))
        token = bytes(self.token,'utf-8')
        message = data_type+token+message
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