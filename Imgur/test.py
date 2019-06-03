import requests
import base64
import json

# image_file = open("test.jpg", "rb")
# image_data = image_file.read()
# url = 'https://api.imgur.com/3/upload'
# data = {'image': image_data, 'title': 'test'}
# files = {}
# client_id = "88d20b231064ed2"
# headers = {'Authorization': 'Client-ID ' + client_id}
# response = requests.request('POST', url = url, data = data, headers = headers)
# respone_json = json.loads(response.text)
# print(respone_json['data']['link'])

import requests

url = "https://uksouth.api.cognitive.microsoft.com/face/v1.0/detect"

querystring = {"returnFaceId":"true","returnFaceLandmarks":"false","returnFaceAttributes":"gender","returnFaceAttributes":"age"}
faces = json.dumps({
    "url":"https://pbs.twimg.com/profile_images/914554512571998209/_XkwiN-m_400x400.jpg"
    })
payload = faces
headers = {
    'Content-Type': "application/json",
    'Ocp-Apim-Subscription-Key': "937cc80c20954a35aef1aa76fb8f63b3",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)