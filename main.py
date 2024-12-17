import time
import system
import argparse
from statistics import mode
import json
import sys, getopt
import threading

FILE_KONFIGURASI = "./config.conf"
DEBUG = False

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
    sensor1 = sistem.init_sensor('sensor1')
    sensor_thread = threading.Thread(target=sensor1.sensor_loop)
    sensor_thread.daemon = True
    sensor_thread.start()

    # video stream setup
    stream_port = int(sistem._config['video_server']['port'])
    stream_camera = sistem._config['video_server']['camera']
    streamer = system.video_sender(sistem._config[stream_camera]['link'],sistem._config['video_server']['address'],stream_port)
    streamer.token = sistem._config['general']['token']
    streamer.debug = DEBUG
    
    # sensor1.thread.start() # mulai sensor
    print("Starting services")
    # sensor start
    
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
