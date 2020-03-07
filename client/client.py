from __future__ import print_function
import requests
import json
import numpy as np
import cv2

addr = 'http://localhost:5001'
test_url = addr + '/api/flip'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

print("reading image now")

img = cv2.imread('nice.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpeg', img)
print("sending data out")
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
# convert string of image data to uint8
# print(response.text)
# jsonTree = json.loads(response.text)
# imjson = str(jsonTree['data'])
print(response.content)
nparr = np.fromstring(response.content, np.uint8)
# # decode image
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

# cv2.imwrite("fliped.jpg", img)
# nparr = np.fromstring(json.loads(response.text), np.uint8)
# print(nparr)
# # decode image
# img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imwrite("edited/fliped.jpg", img)

# expected output: {u'message': u'image received. size=124x124'}