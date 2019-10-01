'''
# Dependencies
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

X = np.array([[5, 3],
              [10, 15],
              [15, 12],
              [24, 10],
              [30, 30],
              [85, 70],
              [71, 80],
              [60, 78],
              [70, 55],
              [80, 91]])

# Plot
labels = range(1, 11)
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:, 0], X[:, 1], label='True Position')
for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(-3, 3),
                 textcoords='offset points', ha='right', va='bottom')



# Dendogram
linked = linkage(X, 'single')
labelList = range(1, 11)
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()
'''

'''
# Dependices
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np

X = np.array([[5, 3],
              [10, 15],
              [15, 12],
              [24, 10],
              [30, 30],
              [85, 70],
              [71, 80],
              [60, 78],
              [70, 55],
              [80, 91]])

cluster = AgglomerativeClustering(
    n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster.labels_, cmap='rainbow')
plt.show()
'''

import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as shc

customer_data = pd.read_csv('shopping_data.csv')

print("*** Customer Data Shape ***")
print(customer_data.shape)
print('\n')

print("*** Customer Data Head ***")
print(customer_data.head())
print('\n')

data = customer_data.iloc[:,3:5].values

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()


# *** QUESTIONS ***

# 1. How many clusters do you have? Explain your answer.
#   Filtering the outliers on the dendogram we agreed on 5 clusters.
# 
# 2. Plot the clusters to see how actually the data has been clustered.
#   Plot shown above.
#
# 3. What can you conclude by looking at the plot?
#   There's five clusters and some outliers to the right of the plot. 
