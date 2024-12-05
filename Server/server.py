import cv2
import socket
import redis
import mysql.connector
import threading
import base64
import json
import flask
import time
from hashlib import sha256
import var
import sys, getopt

DEBUG = False

class server:
    def __init__(self,listen_addresses="0.0.0.0",listen_port = 8000,api_port=8008):
        self.no_image = var.no_img
        self.api_port = api_port
        self.redis_host = 'redis'
        self.redis_port = 6379
        self.redis_server = redis.Redis(host=self.redis_host, port=self.redis_port, decode_responses=True)
        self.BUFF_SIZE = 655360
        self.socket_address = (listen_addresses,listen_port)
        self.debug = False
        self.mysql_host = 'database'
        self.mysql_user = 'app'
        self.mysql_pass = 'password'
        self.mysql_db = 'water_level'
        self.mysql_server = mysql.connector.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_pass,
            database=self.mysql_db,
            
        )

        self.load_dev_addr()
        pass

    def load_dev_addr(self):
        cursor = self.mysql_server.cursor(buffered=True)
        # eksekusi pengambilan token
        cursor.execute("SELECT token, dev_id FROM `dev_auth`")
        # simpan hasil pencarian token
        self.dev_auth = cursor.fetchall()
        if (self.debug) :
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
    
    def video_stream(self):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
        server_socket.bind(self.socket_address)
        print('Listening at :',self.socket_address)
        while (True):
            # ambil data
            msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
            kode = msg[0:1]
            token = msg[1:65]
            token = token.decode("utf-8")
            address = self.check_address(token)

            # status = dev_addr.check_address(address)
            if address != False:
                data = msg[65:]
                # print(img)
                if(kode == b'1'):
                    self.redis_server.set(address,data)
                if(kode == b'2'):
                    decoded = base64.b64decode(data)
                    address = address+"_data"
                    self.redis_server.set(address,decoded)

    def server_maintance(self):
        timer = 0;
        while True:
            if(timer >= 60):
                timer = 0;
                self.load_dev_addr()
            time.sleep(1)
        
    def start(self):
        self.thread = threading.Thread(target=self.video_stream)
        self.maintence_thread = threading.Thread(target=self.server_maintance)
        self.maintence_thread.daemon =True
        self.thread.daemon = True
        self.maintence_thread.start()
        self.thread.start()
    
    def get_option_value(self,option = ''):
        # ambil option dari mysql server
        cursor = self.mysql_server.cursor(buffered=True)
        cursor.execute("SELECT value FROM `options` WHERE `name` =  %s",(option,))
        result = cursor.fetchall()

        if(len(result) == 1):
            value = result[0][0]
        else:
            value = False
        cursor.close()
        return value

    def gen_dev_token(self,dev_id,dev_timestamp=time.time()):
        token = ''
        # get server key
        server_key = self.get_option_value('server_key')
        if(server_key != False):
            input_ = dev_id+server_key+str(dev_timestamp)
            token = sha256(input_.encode('utf-8')).hexdigest()
        # cursor.execute
        return token
    
    def get_image(self,dev_id=""):
        if(dev_id == ""):
            return self.no_image
        data = self.redis_server.get(dev_id)
        if data:
            return data
        else:
            return self.no_image

    def get_data_realtime(self,def_id = ""):
        if(def_id == ""):
            return ""
        data = self.redis_server.get(def_id+'_data')
        if data :
            return data
        else :
            return ""
    
    def add_device(self,dev_id=''):
        pass
        
server_ = server()

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "hello"

@app.route('/api/get/image/<string:dev_id>/')
def get_image(dev_id=""):
    if dev_id == "":
        return "Bad Request"
    return server_.get_image(dev_id)

@app.route('/api/get/data_realtime/<string:def_id>/')
def get_data_realtime(def_id = ""):
    if(def_id == ""):
        return ""
    return server_.get_data_realtime(def_id)

@app.route('/api/dev/v1')
def def_api():
    res = ''
    return res

@app.route('/api/dev/v1/status/<string:def_id>/')
def def_status(def_id = ""):
    ret = ''
    return ret


if __name__ == '__main__':
    ARGList = sys.argv[1:]
    # Options
    options = "hf:d"
    long_options = ["Help", "file_konfig", "debug"]
    try:
        arguments, values = getopt.getopt(ARGList, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print("help")
                sys.exit()
            elif currentArgument in ("-f", "--file_konfig"):
                FILE_KONFIGURASI = currentValue
                print("Menggunakan file konfigurasi di "+FILE_KONFIGURASI)
            elif currentArgument in ("-d", "--debug"):
                print("DEBUG ACTIVATED!")
                DEBUG = True
    except getopt.error as err:
        print(str(err))
        sys.exit()
    
    server_.start()
    app.run(debug=DEBUG,port=8008,host='0.0.0.0')