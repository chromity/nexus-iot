import time
import requests
import json

lat = [
    14.534283,
    14.534353,
    14.534467,
    14.534509,
    14.534623,
    14.534737,
    14.534882,
    14.535022,
    14.535128,
    14.535234,
    14.535377,
    14.535494,
    14.535619,
    14.535762,
    14.535889,
    14.536011,
    14.536136,
    14.536253,
    14.536319,
    14.536415,
    14.536589,
    14.536688,
    14.536784,
    14.536885,
    14.537012,
    14.537129,
    14.537344,
    14.537669,
    14.537918,
    14.537918,
    14.538188,
    14.538416,
    14.538598,
    14.538829,
    14.538951,
    14.539094,
    14.539094,
    14.539223,
    14.539266,
    14.539340,
    14.539396,
    14.539473,
    14.539547,
    14.539639,
    14.539732,
    14.539831,
    14.539880,
    14.539967,
    14.540047,
    14.540144,
    14.540228,
    14.540328,
    14.540416,
    14.540471,
    14.540522,
    14.540612,
    14.540685,
    14.540749,
    14.540829,
    14.540925,
    14.540991, 
    14.541066,
    14.541153,
    14.541204,
    14.541287,
    14.541366,
    14.541436,
    14.541644,
    14.541721,
    14.541813,
    14.541901,
    14.542004,
    14.542165,
    14.542344,
    14.542510,
    14.542510,
    14.542699,
    14.542889,
    14.543028,
    14.543120,
    14.543265,
    14.543355,
    14.543414,
    14.543552,
    14.543686,
    14.543785,
    14.543894,
    14.544052,
    14.544280,
    14.544459,
    14.544565, 
    14.544668,
    14.545127,
    14.545275,
    14.545548,
    14.545839,
    14.546078,
    14.546403,
    14.546572,
    14.546811,
    14.547076,
    14.547237,
    14.547414,
    14.547565,
    14.547705
    ]
while True:
    for each in lat:
        sensor_data = {
            "$class": "org.nexus.basic.SetLocationLat",
            "lat": "resource:org.nexus.basic.Sensor#02A",
            "newLocationLat": str(each)
            }
        r = requests.post("http://178.128.16.137:3000/api/org.nexus.basic.SetLocationLat", data=sensor_data)
        print(r.json)
        time.sleep(1)
