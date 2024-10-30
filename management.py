import requests

class client:
    def __init__(self,url,key):
        self.url = url
        self.key = key
        
    def download_config(self):
        pass
    
    def send_image(self):
        url = self.url+'?payload='+self.key
        files = {'media': open('test.jpg', 'rb')}
        response = requests.post(url,files=files)
        
    def send_sensor(self):
        url = self.url+'?payload='+self.key
        response = requests.get(url)
        pass