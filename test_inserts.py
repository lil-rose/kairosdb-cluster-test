"""
@author: Rosita Hormann

Python 3.7.4
"""
# Imports:
import requests
from random import randrange
import time
import numpy as np


host="localhost"
port="8080" #8080 and 8081 are KairosDB nodes, 80 is Nginx node.
api_base = "http://"+ host +":" + port +"/api/v1"

#current_date = np.round(time.time()*1000,0) # time.time() is in seconds
current_date = 1577836800000 # 01-jan-2020 00:00:00 (timestamp in milliseconds)
metric_name = "example_2"
tags = {
        "host": "host_example"
        }

list_datapoints = []

n_datapoints = 3000 # number of datapoints to insert

for i in range(n_datapoints):
    value = randrange(1000)
    data_point = [current_date, value]
    list_datapoints.append(data_point)
    
    current_date += 1000

data_to_post = {
                  "name": metric_name,
                  "datapoints": list_datapoints,
                  "tags": tags
                }

start = time.time()
req = requests.post(api_base+"/datapoints", json = data_to_post)
end = time.time()


print("req.status_code", req.status_code)
print("response: ", req)
print("------------------------------------------------------")
print("Insertion time:", end - start, "seconds")