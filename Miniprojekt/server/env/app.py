from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/ping', methods=['POST'])
def receiveMessage():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        # printing result as string 
        print(post_data['data'])
        inputData = post_data['data']

        # DO ML STUFF
    else:
        print('error')
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()