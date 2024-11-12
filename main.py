import time
import water_level_detector
import system
import video_sender

# Load config
sys = system.system('./config.conf')
config = sys._config

if __name__ == '__main__':
    # sensor1_conf = config['sensor1']
    videolink = config['sensor1']['videolink']
    sensor1_tinggi_atas = int(config['sensor1']['sensor1_tinggi_atas'])
    sensor1_tinggi_bawah = int(config['sensor1']['sensor1_tinggi_bawah'])
    sensor1_lebar_kiri = int(config['sensor1']['sensor1_lebar_kiri'])
    sensor1_lebar_kanan = int(config['sensor1']['sensor1_lebar_kanan'])
    sensor1 = water_level_detector.water_level(videolink, sensor1_tinggi_atas, sensor1_tinggi_bawah,sensor1_lebar_kiri,sensor1_lebar_kanan) # penggil sensor
    stream_port = int(config['video_server']['port'])
    streamer = video_sender.video_sender(config['sensor1']['videolink'],config['video_server']['address'],stream_port)
    
    # sensor1.thread.start() # mulai sensor
    print("Starting services")
    sensor1.start()

    # stream video to server
    streamer.start()
    while True:
        print("tinggi permukaan =",sensor1.result)
        time.sleep(2)
# sensor1 = water_level_detector.water_level(videolink, sensor1_tinggi_atas, sensor1_tinggi_bawah,sensor1_lebar_kiri,sensor1_lebar_kanan)
# sensor1.image_look()