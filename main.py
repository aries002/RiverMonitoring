import time
import water_level_detector
import system
import argparse
from statistics import mode
import json
import sys, getopt


FILE_KONFIGURASI = "./config.conf"
DEBUG = False

def sensor_setup(sensor):
    sensor_camrea = config[sensor]['camera']
    camera_link = config[sensor_camrea]['link']

    tinggi_atas = int(config[sensor]['tinggi_atas'])
    tinggi_bawah = int(config[sensor]['tinggi_bawah'])
    lebar_kiri = int(config[sensor]['lebar_kiri'])
    lebar_kanan = int(config[sensor]['lebar_kanan'])

    return water_level_detector.water_level(camera_link, tinggi_atas,tinggi_bawah,lebar_kiri,lebar_kanan)

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
                DEBUG = True
    except getopt.error as err:
        print(str(err))
        sys.exit()
    # Load config
    sistem = system.config(FILE_KONFIGURASI)
    config = sistem._config
    api = system.api_client(config['general']['server_address'])
    
    # sensor setup
    sensor1 = sensor_setup('sensor1')
    sensor1.debug = DEBUG
    # video stream setup
    stream_port = int(config['video_server']['port'])
    stream_camera = config['video_server']['camera']
    streamer = system.video_sender(config[stream_camera]['link'],config['video_server']['address'],stream_port)
    streamer.debug = DEBUG
    
    # sensor1.thread.start() # mulai sensor
    print("Starting services")
    # sensor start
    sensor1.start()

    # stream video to server
    streamer.start()
    # main process
    detik = 0
    tampung_sensor = []
    while True:
        # print("tinggi permukaan =",sensor1.result)
        # ambil data sensor dan kumpulkan selama 1 menit
        if detik < 60:
            tampung_sensor[detik] = sensor1.result # ambil data setiap detik
            detik+1
        else:
            detik = 0
            payload = []
            payload['water_sensor'] = mode(tampung_sensor) # ambil data yang paling sering muncul untuk menghilangkan gangguan
            json_payload = json.dumps(payload) # persiapkan data dalam json
            api.send_sensor(json_payload) # kirimkan data
            if DEBUG :
                print("Sensor Data:")
                print(tampung_sensor)
                print(json_payload)
            tampung_sensor = []
        
        # ambil status dan terapkan perintah
        perintah = api.get_status()
        if perintah == "start_video_stream":
            streamer.run = True
        elif perintah == "stop_video_stream":
            streamer.run = False
        elif perintah == "restart_system"+config["general"]["dev_id"]:
            print("System rebooting in short time")
            time.sleep(3)
        
        time.sleep(1)
