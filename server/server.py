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
    print("get the request!")
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    print("fancy stuffs")
    flip = cv2.flip(img, 0)
    _, img_encoded = cv2.imencode('.jpeg', flip)

    # # _, img_encoded = cv2.imencode('.jpeg', img)
    # # print("saving a fliped image")
    # # Create and add usertoek in the path if needed
    # # cv2.imwrite("tmp/fliped.jpg", flip

    # # build a response dict to send back to client
    # response = {'data': img_encoded.tostring()}
    # # encode response using jsonpickle
    # response_pickled = jsonpickle.encode(response)

    # print("respoding")
    # # return send_file()
    print(img_encoded.tostring())
    return img_encoded.tostring(), 200


# start flask app
app.run(host="0.0.0.0", port=5001)