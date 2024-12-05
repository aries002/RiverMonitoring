import time
from hashlib import sha256
import uuid
import json

server_key = input("Server key : ")
dev_timestamp = time.time()
dev_timestamp = int(dev_timestamp)
dev_id = hex(uuid.getnode())[2:]
dev_id = str(dev_id)
input_ = dev_id+server_key+str(dev_timestamp)

token = sha256(input_.encode('utf-8')).hexdigest()

output = {
    "dev_id" : dev_id,
    "timestamp" : dev_timestamp,
    "token" : token
}

json_out = json.dumps(output)
print(json_out)