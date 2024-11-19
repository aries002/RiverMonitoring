import time
import water_level_detector
import system

# Load config
sys = system.config('./config.conf')
config = sys._config

def sensor_setup(sensor):
    sensor_camrea = config[sensor]['camera']
    camera_link = config[sensor_camrea]['link']

    tinggi_atas = int(config[sensor]['tinggi_atas'])
    tinggi_bawah = int(config[sensor]['tinggi_bawah'])
    lebar_kiri = int(config[sensor]['lebar_kiri'])
    lebar_kanan = int(config[sensor]['lebar_kanan'])

    return water_level_detector.water_level(camera_link, tinggi_atas,tinggi_bawah,lebar_kiri,lebar_kanan)

def system_loop():
    # ambil data sensor
    # ambil data yang paling sering keluar dalam satu periode loop
    # kirimkan data sensor
    # ambil status dan perintah
    # jalankan perintah
    pass

def system_setup():
    pass
    

if __name__ == '__main__':
    # sensor setup
    sensor1 = sensor_setup('sensor1')
    # video stream setup
    stream_port = int(config['video_server']['port'])
    stream_camera = config['video_server']['camera']
    streamer = system.video_sender(config[stream_camera]['link'],config['video_server']['address'],stream_port)
    
    # sensor1.thread.start() # mulai sensor
    print("Starting services")
    # sensor start
    sensor1.start()

    # stream video to server
    streamer.start()
    while True:
        print("tinggi permukaan =",sensor1.result)
        time.sleep(2)
# sensor1 = water_level_detector.water_level(videolink, sensor1_tinggi_atas, sensor1_tinggi_bawah,sensor1_lebar_kiri,sensor1_lebar_kanan)
# sensor1.image_look()