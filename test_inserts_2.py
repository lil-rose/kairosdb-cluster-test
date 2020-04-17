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

metric_base_name = "cpu_"
tags = {
        "host": "host_example"
        }

n_datapoints = 10000 #80000*60*15 # number of datapoints to insert for each time series
n_timeseries = 10 # numbers of time series

total_insertion_time = 0

for j in range(n_timeseries):
    list_datapoints = []
    current_date = 1577836800000 # 01-jan-2020 00:00:00 (timestamp in milliseconds)
    metric_name = metric_base_name + str(j)
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

    print("Metric: ", metric_name)
    print("req.status_code", req.status_code)
    print("response: ", req)
    print("Insertion time:", end - start, "seconds")
    print("------------------------------------------------------")

    total_insertion_time += (end - start)
    
print("TOTAL INSERTION TIME:", total_insertion_time)