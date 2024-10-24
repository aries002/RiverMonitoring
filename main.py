import time
import water_level_detector
import config_helper

# Load config
conf = config_helper.config_helper('./config.conf')
config = conf._config

# videolink = "rtsp://admin:p4ssw0rdAMAN@192.168.77.193:554/Streaming/channels/102"
# sensor1_tinggi_atas = 5
# sensor1_tinggi_bawah = 600
# sensor1_lebar_kiri = 0
# sensor1_lebar_kanan = 43

if __name__ == '__main__':
    # sensor1_conf = config['sensor1']
    videolink = config['sensor1']['videolink']
    sensor1_tinggi_atas = int(config['sensor1']['sensor1_tinggi_atas'])
    sensor1_tinggi_bawah = int(config['sensor1']['sensor1_tinggi_bawah'])
    sensor1_lebar_kiri = int(config['sensor1']['sensor1_lebar_kiri'])
    sensor1_lebar_kanan = int(config['sensor1']['sensor1_lebar_kanan'])
    sensor1 = water_level_detector.water_level(videolink, sensor1_tinggi_atas, sensor1_tinggi_bawah,sensor1_lebar_kiri,sensor1_lebar_kanan) # penggil sensor
    sensor1.thread.start() # mulai sensor
    print("Start")
    while True:
        print("tinggi permukaan =",sensor1.result)
        time.sleep(2)
# sensor1 = water_level_detector.water_level(videolink, sensor1_tinggi_atas, sensor1_tinggi_bawah,sensor1_lebar_kiri,sensor1_lebar_kanan)
# sensor1.image_look()