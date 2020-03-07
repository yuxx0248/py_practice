from flask import Flask, request
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/flip', methods=['POST'])
def test():	
    r = request
    print("get the request! starting decode image from request message")
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do your image process logic here....
    print("fliping yo yo yo")
    flip = cv2.flip(img, 0)

    print("finish fliping, encode for transmission")
    _, img_encoded = cv2.imencode('.jpeg', flip)

    print("all set, responding with image binary as string")
    return img_encoded.tostring(), 200


# start flask app
app.run(host="0.0.0.0", port=5001)