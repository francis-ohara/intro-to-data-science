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


# from sklearn.datasets import make_blobs
# import matplotlib.pyplot as plt
#
# samples, clusters = make_blobs(centers=4)
#
# x_values = samples[:, 0]
# y_values = samples[:, 1]
#
# plt.scatter(x_values, y_values, c=clusters)
# plt.show()


# #  Can value of attribute be user-defined object?
# class Test:
#     value = "Hello world!"
#
#
# class Test2:
#     value = Test()
#
#
# test2 = Test2()
# print(test2.value.value)


import matplotlib.pyplot as plt
import matplotlib

#
# mpl.style.use("default")
# plt.plot([1, 2, 3, 4, 5], [6, 19, 29, 45, 23])
# plt.show()
#
# plt.plot([1,2,3,4,5], [6, 19, 29, 45, 23])
# plt.show()
# print(type(matplotlib.style.available))

import numpy as np
import matplotlib.pyplot as plt

temperatures = [37, 28, 33, 35, 18, 9, 89, 34, -12, 40]

# calculating percentiles
percentile10 = np.percentile(temperatures, 10)
percentile90 = np.percentile(temperatures, 90)

# box plot before imputation
plt.boxplot(temperatures, vert=False)
plt.title("Before Imputation")
plt.show()


# imputing outliers
for i in range(len(temperatures)):
    if temperatures[i] < percentile10:
        temperatures[i] = percentile10
    elif temperatures[i] > percentile90:
        temperatures[i] = percentile90
    i+= 1



# box plot after imputation
plt.boxplot(temperatures, vert=False)
plt.title("After Imputation")
plt.show()
