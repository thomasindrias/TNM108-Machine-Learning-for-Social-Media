from flask import Flask, jsonify, request
from flask_cors import CORS
from summarizer import TextSummarizer
import json

# configuration
DEBUG = True

#Data 
predicted_data = None
typeOfSummarization = None

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['POST'])
def receiveMessage():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        
        # printing result as string 
        # print(post_data['data'])
        inputData = post_data['data']
        typeOfSummarization = post_data['data_type']
        print('type of Summarization ' + typeOfSummarization)
        global predicted_data
        predicted_data = ML(inputData, typeOfSummarization)
        
    else:
        print('error')
    return jsonify(response_object)

def ML(data, typeOfSummarization):
    text_input = []
    text_input.append(data)

    print('Using:' + typeOfSummarization)

    if typeOfSummarization == 'book':
        predicted_data = book_summarizer.predict(text_input)
    elif typeOfSummarization == 'food':
        predicted_data = food_summarizer.predict(text_input)    

    return predicted_data

# Send back summarization
@app.route('/ping', methods=['GET'])
def returnSummarization():
    global predicted_data
    return jsonify(predicted_data)

def init_summarizer (data_file_name):
    # Set paths to pretrained models
    encoder_model_path = "./models/encoder_model_" + data_file_name + ".h5"
    decoder_model_path = "./models/decoder_model_" + data_file_name + ".h5"
    # Set paths to corresponding tokenizers
    x_tokenizer_path = "./models/x_tokenizer_" + data_file_name + ".pickle"
    y_tokenizer_path = "./models/y_tokenizer_" + data_file_name + ".pickle"

    return TextSummarizer(encoder_model_path, decoder_model_path, x_tokenizer_path, y_tokenizer_path)

if __name__ == '__main__':
    # Name of the processed data
    book = "Kindle_Reviews_Processed_200k"
    food = "Food_Reviews_Processed_200k"

    # Initialize the summarizer with preloaded models and corresponding tokenizers
    book_summarizer = init_summarizer(book)
    food_summarizer = init_summarizer(food)
    
    app.run()