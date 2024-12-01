import cv2
import base64
import mysql.connector
import redis
import numpy as np

store = redis.Redis(host='localhost', port=6379, decode_responses=True)
mysql_server = mysql.connector.connect(
  host="127.0.0.1",
  user="app",
  password="password",
  database="water_level"
)

def show_video():
    cursor = mysql_server.cursor(buffered=True)
    sql = "SELECT id, nama FROM device"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    while True:
        for (id,nama) in result :
            data = store.get(id)
            if data :
                # print("valid frame from ",addr)
                decoded = base64.b64decode(data)
                npdata = np.frombuffer(decoded, dtype=np.uint8)
                frame = cv2.imdecode(npdata,1)
                title = "IMAGE FROM "+nama
                cv2.imshow(title, frame)
                if cv2.waitKey(0) == ord('q'):
                    break
show_video()