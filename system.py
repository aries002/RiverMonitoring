import os
import configparser
import cv2
import requests

DEF_LOCATION = ""
DEF_TEMPLATE = './config_template.conf'

URI_CONFIG = ''
URI_SENSOR = ''
URI_TIMELAPSE = ''


class system:
    def __init__(self, config_location = ''):
        self.def_if = 'testing'
        self.config_location =config_location
        if config_location == '':
            config_location = DEF_LOCATION
        if not os.path.isfile(config_location):
            self.create_conf()
        self._config = configparser.ConfigParser()
        self._config.read(config_location)
    
    def create_conf(self):
        new_config = configparser.ConfigParser()
        if not os.path.isfile(DEF_TEMPLATE):
            print("Template not found exiting")
        else:
            new_config.read(DEF_TEMPLATE)
            with open(self.config_location, 'w') as configfile:
                new_config.write(configfile)
                configfile.close()

    def print_config(self):
        #  data in self.data:?
        for section in self._config.sections():
            print('[',section,']')
            for config in self._config[section]:
                print(config, "=", self._config[section][config],'(',type(self._config[section][config]),')')
        # print(self._config.sections())
    
    def get_config(self):
        pass
    
    def send_image(self,img_url):
        url = self._config['server']['url']+URI_TIMELAPSE
        dev_id = self._config['server']['dev_id']
        key = self._config['server']['key']
        
        # get image
        vid = cv2.VideoCapture(img_url)
        result, image = vid.read()

        # prepare data
        data = {'dev_id' : dev_id, 'key' : key}
        files = {'timelapse' : image}

        # send data
        response = requests.post(url, files = files, data = data)
        if(response.status_code == 200):
            return True
        else:
            return False


    def send_sensor(self, json_value):
        url = self._config['server']['url']+URI_SENSOR
        dev_id = self._config['server']['dev_id']
        key = self._config['server']['key']

        # prepare data
        body = json_value
        
        pass

    def get_status(self):
        pass
    