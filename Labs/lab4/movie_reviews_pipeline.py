import sklearn
from sklearn.datasets import load_files

moviedir = r'./movie_reviews'

# loading all files. 
movie = load_files(moviedir, shuffle=True)

from sklearn.model_selection import train_test_split
docs_train, docs_test, y_train, y_test = train_test_split(movie.data, movie.target, 
                                                          test_size = 0.20, random_state = 12)

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
import nltk

text_clf = Pipeline([
 ('vect', CountVectorizer(min_df=2, tokenizer=nltk.word_tokenize, max_features=3000)),
 ('tfidf', TfidfTransformer()),
 ('clf', MultinomialNB()),
])

text_clf.fit(movie.data, movie.target)
predicted = text_clf.predict(docs_test)
print("multinomialBC accuracy ",np.mean(predicted ==  movie.target))
