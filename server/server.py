from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():	
    r = request
    print("get the request!")
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    print("fancy stuffs")
    _, img_encoded = cv2.imencode('.jpeg', img)

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    print("respoding")
    # return send_file()
    return Response(response=response_pickled, data=img_encoded.tostring(), atus=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)