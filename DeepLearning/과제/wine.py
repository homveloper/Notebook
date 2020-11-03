from sklearn.datasets import load_wine
import numpy as np

wine = load_wine()

print(wine.data.shape)
print(wine.target.shape)
print(len(np.unique(wine.target)))