import pandas as pd
import matplotlib.pyplot as plt

trainset = pd.read_csv(r"DeepLearning\04 학습데이터 살펴보기\trainset.csv",dtype='float')

trainset.plot.scatter(x='x',y='z')
plt.show()
