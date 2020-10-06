import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

## 학습데이터와 평가데이터 분리

iris = load_iris(as_frame=True)
x = iris.data
y = iris.target

x['class'] = pd.Series(y)

train_set, test_set = train_test_split(x, train_size = 0.8, random_state = 15,stratify=y)

x_train = train_set.drop('class',axis=1)
y_train = train_set['class'].copy()

x_test = test_set.drop('class',axis=1)
y_test = test_set['class'].copy()

print(len(x_train),len(y_train),len(x_test),len(y_test))

## 학습데이터와 평가데이터에서 입출력분리

iris = load_iris(as_frame=True)
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test =train_test_split(x,y, train_size = 0.8, random_state = 15,stratify=y)

_,c_test = np.unique(y_test,return_counts=True)
_,c_train = np.unique(y_train,return_counts=True)

print(c_test,c_train)   # iris class별 갯수
print(c_test/(c_train+c_test))  #iris class 균일도

## 학습데이터와 평가데이터의 입력데이터 스케일링

scaler = StandardScaler()
scaled_x_train = scaler.fit_transform(x_train)
scaled_x_test = scaler.transform(x_test);

print("평균", " : ", scaler.mean_)
print("편차", " : ", scaler.var_)

## 학습데이터와 평가데이터의 출력데이터 원핫인코딩

encoder = OneHotEncoder()
onehot_y_train = encoder.fit_transform(pd.Series.to_numpy(y_train,copy=True).reshape(-1,1))
onehot_y_test = encoder.transform(pd.Series.to_numpy(y_test,copy=True).reshape(-1,1))

print(scaled_x_train)
print(scaled_x_test)

print("학습 레이블 원핫")
print(onehot_y_train.toarray())
print("평가 레이블 원핫")
print(onehot_y_test.toarray())