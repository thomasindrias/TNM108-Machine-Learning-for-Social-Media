# Import libraries
import pickle # For saving/loading tokenizers
import tensorflow as tf 
import numpy as np  
import pandas as pd
pd.set_option("display.max_colwidth", 200)

import warnings
warnings.filterwarnings("ignore")

from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences  
#from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from keras import backend as K 

# Import custom third-party attention layer
from attention import AttentionLayer
from cleaner import DataCleaner

class TextSummarizer(object):
    """description of class"""
    def __init__(self, encoder_model_path, decoder_model_path, x_tokenizer_path, y_tokenizer_path): 
        # From the histogram we saw that most reviews has the length 80 and summaries has length 10
        self.max_len_text=80 
        self.max_len_summary=10

        # Load review tokenizer
        with open(x_tokenizer_path, 'rb') as handle:
            self.x_tokenizer = pickle.load(handle)

        # Load summary tokenizer
        with open(y_tokenizer_path, 'rb') as handle:
            self.y_tokenizer = pickle.load(handle)

        # Build the dictionary to convert the index to word for target and source vocabulary
        self.reverse_target_word_index = self.y_tokenizer.index_word 
        self.reverse_source_word_index = self.x_tokenizer.index_word 
        self.target_word_index = self.y_tokenizer.word_index

        # Load the pre-trained models
        self.encoder_model = tf.keras.models.load_model(encoder_model_path, custom_objects={'AttentionLayer': AttentionLayer})
        self.decoder_model = tf.keras.models.load_model(decoder_model_path, custom_objects={'AttentionLayer': AttentionLayer})

    def decode_sequence(self, input_seq):
        # Make sure the input sequence is not longer than max text length
        input_seq = input_seq.reshape(1, self.max_len_text)

        # Encode the input as state vectors
        e_out, e_h, e_c = self.encoder_model.predict(input_seq)

        # Generate empty target sequence of length 1.
        target_seq = np.zeros((1,1))

        # Chose the 'start' word as the first word of the target sequence
        target_seq[0, 0] = self.target_word_index['start']

        stop_condition = False
        decoded_sentence = ''
        while not stop_condition:
            output_tokens, h, c = self.decoder_model.predict([target_seq] + [e_out, e_h, e_c])

            # Sample a token
            sampled_token_index = np.argmax(output_tokens[0, -1, :])

            # Exit if sample_token_index is 0
            if (sampled_token_index == 0):
                stop_condition = True
            else:
                sampled_token = self.reverse_target_word_index[sampled_token_index]

                if(sampled_token != 'end'):
                    decoded_sentence += ' ' + sampled_token

                    # Exit condition: Hit max length
                    if (len(decoded_sentence.split()) >= (self.max_len_summary-1)):
                        stop_condition = True
            

            # Update the target sequence (of length 1).
            target_seq = np.zeros((1,1))
            target_seq[0, 0] = sampled_token_index

            # Update internal states
            e_h, e_c = h, c

        return decoded_sentence

    # Use test batch to predict summaries and compare with original
    def predict_test_data(self, data_file_path, count):
        # Load data
        data = pd.read_csv(data_file_path)
        data['Summary'].replace('', np.nan, inplace=True)
        data.dropna(axis=0, inplace=True)
        # Add special tokens START in the beginning and END at the end of all summaries
        data['Summary'] = data['Summary'].apply(lambda x : '_START_ '+ x + '_END_')

        # Split the dataset into a training and validation set (90% train, 10% test, not random since it should be the same as the trained model)
        x_train, x_validation, y_train, y_validation = train_test_split(data['Text'], data['Summary'], test_size=0.1, random_state=0, shuffle=True)

        # Convert string sequences into integer sequences
        x_validation = self.x_tokenizer.texts_to_sequences(x_validation)
        # Padding zero to maximum length
        x_validation = pad_sequences(x_validation, maxlen=self.max_len_text, padding='post')

        # Convert string sequences into integer sequences 
        y_validation = self.y_tokenizer.texts_to_sequences(y_validation) 
        # Padding zero to maximum length
        y_validation = pad_sequences(y_validation, maxlen=self.max_len_summary, padding='post')
        
        for i in range(count):
          print("Review:", self.__seq2text(x_validation[i]))
          print("Original summary:", self.__seq2summary(y_validation[i]))
          print("Predicted summary:", self.decode_sequence(x_validation[i]))
          print("\n")

    def predict(self, texts):
        # Clean the texts
        cleaned_text = []
        for t in texts:
            cleaned_text.append(DataCleaner.clean_text(t))

        # Convert texts to integer sequences with tokenizer
        sequences = self.x_tokenizer.texts_to_sequences(cleaned_text)
        sequences = pad_sequences(sequences, maxlen=self.max_len_text, padding='post')

        for i in range(len(texts)):
            print("Review:", texts[i])
            print("Predicted summary: ", self.decode_sequence(sequences[i]))
            print("\n")

    # Convert integer sequence to summary sequence
    def __seq2summary(self, input_seq):
        newString = ''
        for i in input_seq:
          if((i!=0 and i!=self.target_word_index['start']) and i!=self.target_word_index['end']):
            newString = newString + self.reverse_target_word_index[i] + ' '
        return newString

    # Convert integer sequence to text sequence
    def __seq2text(self, input_seq):
        newString = ''
        for i in input_seq:
          if(i!=0):
            newString = newString + self.reverse_source_word_index[i] + ' '
        return newString




