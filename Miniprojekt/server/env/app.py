from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

#Data 
inputData = None

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# def __init__(self):
#         self.myname = "harry"

@app.route('/ping', methods=['POST'])
def receiveMessage():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        # printing result as string 
        print(post_data['data'])
        global inputData 
        inputData = post_data['data']
        # DO ML STUFF
        
    else:
        print('error')
    return jsonify(response_object)

def ML_stuff():
    print("ML stuff")

# Send back summarization
@app.route('/ping', methods=['GET'])
def ping_pong():
    global inputData
    return jsonify(inputData)


if __name__ == '__main__':
    app.run()