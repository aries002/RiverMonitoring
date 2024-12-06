import time
import water_level_detector
import system
import argparse
from statistics import mode
import json
import sys, getopt


FILE_KONFIGURASI = "./config.conf"
DEBUG = False

def sensor_setup(sensor,config):
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
                print("DEBUG ACTIVATED!")
                DEBUG = True
    except getopt.error as err:
        print(str(err))
        sys.exit()


    # Load config
    sistem = system.system(FILE_KONFIGURASI)
    sistem.debug = DEBUG


    # sensor setup
    sensor1 = sensor_setup('sensor1',sistem._config)
    sensor1.debug = DEBUG

    # video stream setup
    stream_port = int(sistem._config['video_server']['port'])
    stream_camera = sistem._config['video_server']['camera']
    streamer = system.video_sender(sistem._config[stream_camera]['link'],sistem._config['video_server']['address'],stream_port)
    streamer.token = sistem._config['general']['token']
    streamer.debug = DEBUG
    
    # sensor1.thread.start() # mulai sensor
    print("Starting services")
    # sensor start
    sensor1.start()

    # stream video to server
    streamer.start()
    # main process
    print("Strating main process")
    while True:

        # kirimkan data realtime
        data_real = {
            "sensor1" :sensor1.result
        }
        data_json = json.dumps(data_real)
        streamer.send_data(data_json)
        # delay 1 detik
        time.sleep(1)
