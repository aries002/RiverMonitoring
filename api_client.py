import requests
import cv2
class client:
    def __init__(self,url):
        self.url = url
        self.uri = {
            'image' : '',
            'status' : '',
            'sensor_data' : '',
            'recent_image' : ''
        }
        self.header ={}
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

    