from typing import Iterator
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

iris = datasets.load_iris()

# iris_keys([
#   'data', 
#   'target', 
#   'frame', 
#   'target_names', 
#   'DESCR', 
#   'feature_names', 
#   'filename'
# ])


iris_target = iris["target"][(iris["target"] == 0)|(iris["target"] == 1)]
iris_target = pd.DataFrame(iris_target,columns=["target"])
print(iris_target)
mapping = {
    0:'setosa',
    1:'versicolor',
    2:'virginica'
}
iris_target["target"] = iris_target["target"].map(mapping)
print(iris_target)
# 抓 sepal length (cm)、petal length (cm) 
iris_data = iris["data"]
iris_data = pd.DataFrame(iris_data,columns=iris["feature_names"])
print(iris_data)
iris_data = iris_data[["sepal length (cm)","petal length (cm)"]]
print(iris_data)
iris_data = pd.concat([iris_data,iris_target],axis=1)
iris_data = iris_data.dropna()
print(iris_data)
mapping = {
    'setosa':1,
    'versicolor':-1
}

# 不符合條件的會直接被 drop 掉
iris_data["target"] = iris_data["target"].map(mapping)

print(iris_data)

#os.system("pause")

# Activation function ( 激勵函數 )
def activation(z):
    return 1 if z>0 else -1

def visualization():
    pass

# w ( 權重 ) 長度需與特徵數一樣
# 在這裡特徵為 [x0,sepal_length,sepal_width]
# x0 永遠為 1
w = np.array([0.,0.,0.])
error = 1 # 錯誤次數
iterator = 0 # 迭代器
while error != 0:
    error = 0
    for i in range(len(iris_data)):
        """
        x : Input
        y : True class label
        """
        x0 = np.array([1.])
        features = np.array(iris_data.iloc[i])[:2]# np.iloc[i] : 抓第 i 行資料
        x = np.concatenate((x0,features))

        y = np.array(iris_data.iloc[i])[2]
        
        result = activation(np.dot(w,x))

        if result != y:
            error += 1
            iterator += 1
            w += y*x
        
    print(error,w,x,y,result,np.dot(w,x))
    

print("End")
