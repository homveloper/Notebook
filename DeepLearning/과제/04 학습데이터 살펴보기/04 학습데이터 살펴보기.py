import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import numpy as np

boston = load_boston()
trainset = pd.DataFrame(data=boston['data'],columns=boston['feature_names'])
trainset['MEDV'] = pd.Series(boston['target'])

# trainset.info()

head = trainset.head()
tail = trainset.tail()

print(head)
# print("===================================================================================================")
print(tail)
# print("===================================================================================================")
describe = trainset.describe()
print(describe)

trainset.hist(layout=(2,7))
plt.show()

trainset.plot(kind="scatter", x='MEDV',y='CRIM')
plt.show()