import json
import requests

"""
Info about KairosDB Rest API:

https://kairosdb.github.io/docs/build/html/QueryingData.html

https://kairosdb.github.io/docs/build/html/restapi/index.html

List of useful methods for this test:

GET http://[host]:[port]/api/v1/version

GET http://[host]:[port]/api/v1/metricnames

GET http://[host]:[port]/api/v1/datapoints/query?query=[encoded_JSON]
JSON simplest example =
{
   "start_absolute": 1357023600000,
   "time_zone": "Asia/Kabul",
   "metrics": [
       {
           "tags": {
               "host": ["foo", "foo2"],
               "customer": ["bar"]
           },
           "name": "abc.123",
       },
   ]
}

It is also allowed to make this request with POST method. he POST version takes the query JSON in the body of the request.




"""

host="localhost"
port="8080"
api_base = "http://"+ host +":" + port +"/api/v1"
req = requests.get(api_base+"/version")

response = req.json()
print(response)