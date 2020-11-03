import pandas as pd
import tflearn
from sklearn.datasets import load_digits
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

digits = load_digits()
minMaxScaler = MinMaxScaler()

# 데이터셋 스케일링
x_data = minMaxScaler.fit_transform(digits.data)
y_data = digits.target

# 데이터 학습용과 테스트용으로 분리
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=3, stratify=y_data)

enc = OneHotEncoder(handle_unknown='ignore')
y_train = enc.fit_transform(y_train.reshape(-1,1)).toarray()
y_test = enc.fit_transform(y_test.reshape(-1,1)).toarray()

# 학습 패러미터 설정
parameter = {
    "n_inputs" : digits.data.shape[1],
    "n_outputs" : len(np.unique(digits.target)),
    "n_epochs" : 200,
    "batch_size" : 20,
    "num_trains" : len(x_train),
    "learning_rate" : 0.01
}

FULLY_CONNECTED = 0
DROPOUT = 1

# 은닉층 설정
dense = {
    # 0 : fully_connected
    # 1 : dropout

    "nodes" : [[0,32],[1,0.5],[0,32],[1,0.5],[0,32],[1,0.5]],
    "activation" : "relu",
    "weights_init" : tflearn.initializations.variance_scaling()
}

# DNN
inputs = tflearn.input_data(shape=(None, parameter["n_inputs"]), name="inputs") 

hiddens = []
for i,node in enumerate(dense["nodes"]):

    if(node[0] == FULLY_CONNECTED):
        hiddens.append(
            tflearn.fully_connected( hiddens[i-1] if i > 0 else inputs ,node[1], activation=dense["activation"], name=f"dense{i}", weights_init=dense['weights_init']))
        
        hiddens.append(
            tflearn.batch_normalization(hiddens[i])
        )

    if(node[0] == DROPOUT):
        hiddens.append(
            tflearn.dropout(hiddens[i-1] if i > 0 else inputs, node[1], name=f"dense_dropout{i}")
        )

softmax = tflearn.fully_connected(hiddens[-1], parameter["n_outputs"], activation='softmax', name ='output', weights_init=dense['weights_init'])

sgd = tflearn.optimizers.SGD(learning_rate=parameter['learning_rate'])
net = tflearn.regression(softmax,optimizer=sgd)

# 모델 생성
model = tflearn.DNN(net,
                tensorboard_verbose=0,
                tensorboard_dir=r"DeepLearning\과제\tflearn_graphs")

# 모델 학습

model.fit(x_train,
          y_train,
          show_metric=True,
          validation_set=None,
        #   snapshot_epoch=True,
          snapshot_step=10,
          n_epoch=parameter["n_epochs"],
          batch_size=parameter["batch_size"])

# 성능 평가
acc_train = model.evaluate(x_train,y_train,parameter["batch_size"])
acc_test = model.evaluate(x_test,y_test,parameter["batch_size"])
print(f"학습 데이터 : {acc_train}, 테스트 데이터 : {acc_test}")

# 모델 저장
model.save(r"DeepLearning\과제\model\model.tfl")

# 모델 로드
model.load(r"DeepLearning\과제\model\model.tfl")

# # 모델 활용
# while (True):
# 	sepal_length = input("sepal length (cm) ? ")
# 	sepal_width = input("sepal width (cm) ? ")
# 	petal_length = input("petal length (cm) ? ")
# 	petal_width = input("petal width (cm) ? ")
# 	new_data = [[sepal_length, sepal_width, petal_length, petal_width]]
# 	predicted = model.predict(new_data)
# 	y_pred = np.argmax(predicted, axis=1)
# 	print(y_pred[0])
