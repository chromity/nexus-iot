import Adafruit_DHT
import time
import requests
import json

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print("Humidity: " + str(humidity) + "\nTemperature: " + str(temperature))
    sensor_data = {
        "$class": "org.nexus.basic.SetSensorTemp",
        "temp": "resource:org.nexus.basic.Sensor#01A",
        "newTemperature": temperature
        }
    r = requests.post("http://178.128.16.137:3000/api/org.nexus.basic.SetSensorTemp", data=sensor_data)
    print(r.json)
    time.sleep(1)
