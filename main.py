# import matplotlib.pyplot as plt
#
#
# plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.show()

# import pandas as pd
#
# x = pd.DataFrame([[1, "hello", 44.5], [2, "world", 50.0], [3, "me", 66.7]])
# print(x)
# print(x[1])

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

samples, clusters = make_blobs(centers=4)

x_values = samples[:, 0]
y_values = samples[:, 1]

plt.scatter(x_values, y_values, c=clusters)
plt.show()

