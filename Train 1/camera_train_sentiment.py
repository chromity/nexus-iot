import argparse

import base64

import picamera

import json

import requests

from googleapiclient import discovery

from oauth2client.client import GoogleCredentials



def takephoto():

    camera = picamera.PiCamera()

    camera.capture('image.jpg')



def main():

    takephoto() # First take a picture

    """Run a label request on a single image"""



    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('vision', 'v1', credentials=credentials)



    with open('image.jpg', 'rb') as image:

        image_content = base64.b64encode(image.read())

        service_request = service.images().annotate(body={

            'requests': [{

                'image': {

                    'content': image_content.decode('UTF-8')

                },

                'features': [{

                    'type': 'FACE_DETECTION',

                    'maxResults': 100

                }]

            }]

        })
        
    response = service_request.execute()
    data_string = json.dumps(response)	#Print it out and make it somewhat pretty
    data = json.loads(data_string)
    sentiment = data['responses'][0]['faceAnnotations'][0]['joyLikelihood']

    sensor_data_sentiment = {
        "$class": "org.nexus.basic.SetSentiment",
        "sent": "resource:org.nexus.basic.Sensor#01A",
        "newSentiment": sentiment
        }
    r = requests.post("http://178.128.16.137:3000/api/org.nexus.basic.SetSentiment", data=sensor_data_sentiment)
    print(r.json)


if __name__ == '__main__':



    main()
