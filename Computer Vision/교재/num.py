import numpy as np

A = np.array([[10,20,30],[20,30,40],[30,40,50]])
B = np.array([[1,2,3],[4,5,6,],[7,8,9]])

print(*(A-B),sep="\n")