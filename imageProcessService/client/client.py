from __future__ import print_function
import requests
import json
import numpy as np
import cv2

addr = 'http://localhost:5001'
flip_url = addr + '/api/flip'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

print("reading image now")
img = cv2.imread('nice.jpg')

# encode image as jpeg
print("encoding image")
_, img_encoded = cv2.imencode('.jpeg', img)

# send http request with image and receive response
print("sending data out and get response back")
response = requests.post(flip_url, data=img_encoded.tostring(), headers=headers)

print("decoding data into images")
# convert content of response data to uint8
nparr = np.fromstring(response.content, np.uint8)
# # decode image
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

print("write respond image into cache for further use")
cv2.imwrite("edited/fliped.jpg", img)
