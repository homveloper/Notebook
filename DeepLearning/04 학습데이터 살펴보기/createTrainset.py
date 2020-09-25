import csv
import numpy as np
import os

def createTrainingSet(filename):
    with open(filename,'w',newline='',encoding='utf-8') as file:
        csvWriter = csv.writer(file,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL);

        csvWriter.writerow(["x","y","z"])

        np.random.seed(4496)

        x = 50 * np.random.rand(100)
        y = 50 * np.random.rand(100)
        z = 3*x + 2*y + 4 + np.random.randn(100)

        for line in zip(x,y,z):
            csvWriter.writerow(line)

createTrainingSet(r'DeepLearning\04 학습데이터 살펴보기\trainset.csv')
     