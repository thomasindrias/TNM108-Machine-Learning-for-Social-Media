# Dependencies
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# print("***** Train_Set *****")
# print(train.head())
# print("\n")

# print("***** Test_Set *****")
# print(test.head())
# print("\n")

# print("***** Train_Set *****")
# print(train.describe())
# print("\n")

# print("***** Column_Values *****")
# print(train.columns.values)
# print("\n")

# For the train set
train.isna().head()
# For the test set
test.isna().head()

# Missing values for train and test set
# print("*****In the train set*****")
# print(train.isna().sum())
# print("\n")
# print("*****In the test set*****")
# print(test.isna().sum())
# print("\n")

# Fill missing values with mean column values in the train set
train.fillna(train.mean(), inplace=True)
# Fill missing values with mean column values in the test set
test.fillna(test.mean(), inplace=True)

# Check if there's still missing values for train and test set
# print("*****In the train set*****")
# print(train.isna().sum())
# print("\n")
# print("*****In the test set*****")
# print(test.isna().sum())
# print("\n")

# print("***** Ticket *****")
# print(train['Ticket'].head())
# print("\n")
# print("***** Cabin *****")
# print(train['Cabin'].head())
# print("\n")

print(train[['Pclass', 'Survived']].groupby(['Pclass'],
                                            as_index=False).mean().sort_values(by='Survived', ascending=False))
print("\n")

print(train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived',
                                                                                     ascending=False))
print("\n")

print(train[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived',
                                                                                         ascending=False))
print("\n")


# Plot histogram
grid = sns.FacetGrid(train, col='Survived', row='Pclass',
                     height=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()
# plt.show()

# data info
# train.info()
# print("\n")

train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

# Let's investigate if you have non-numeric data left
# print("***** Train info *****")
# train.info()
# print("\n")

# print("***** Test info *****")
# test.info()
# print("\n")

# Kmeans model
X = np.array(train.drop('Survived', 1).astype(float))
y = np.array(train['Survived'])


print("***** Kmeans Train info *****")
train.info()
print("\n")

# You want cluster the passenger records into 2: Survived or Not survived
kmeans = KMeans(n_clusters=2)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
       n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
       random_state=None, tol=0.0001, verbose=0)
correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print("***** Model Accuracy *****")
print(correct/len(X))
print("\n")


# *** QUESTIONS ***

# 1. What are the relevant features of the Titanic dataset. Why are they relevant?
#   There is a higher variance for Pclass and Sex.
#      Pclass  Survived
#   0       1  0.629630
#   1       2  0.472826
#   2       3  0.242363
#         Sex  Survived
#   0  female  0.742038
#   1    male  0.188908


# 2. Can you find a parameter configuration to get a validation score greater than 62% ?
# KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
#       n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
#       random_state=None, tol=0.0001, verbose=0)
#
# Current one gives me 0.6262626263??

# 3. What are the advantages/disadvantages of K-Means clustering?
#
#   * Disadvantages
#       - You have to pre specify the number of clusters/centroids, k. (we are not using hiearchical clustering)
#       - it is sensitive to outliers and different results can occur if you change the ordering of the data.
#       -  K-Means starts working only when you trigger it to, thus lazy learning methods can construct a different 
#          approximation or result to the target function for each encountered query.
#       
#   * Advantages
#       - It is a good method for online learning, but it requires a possibly large amount of memory to store the data, 
#         and each request involves starting the identification of a local model from scratch.
#       - For big variables kmeans is most of the time, computationally faster than hiearchical clusters


# 4. How can you address the weaknesses?
#
#   * Sensitive to outliers. 
#       - Can skew your cluster in K means to very large extent.
#       - Can be solved through k median. 
#
#   * Dimensionality.
#       - As K means mostly works on Euclidean distance with increase in dimensions Euclidean distances becomes ineffective. 
#         For a 100 dimensional data everything is far away from each other