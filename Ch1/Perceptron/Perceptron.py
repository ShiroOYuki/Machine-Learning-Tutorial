from typing import Iterator
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Activation function ( 激勵函數 )
def activation(z):
    return 1 if z>0 else -1

# w ( 權重 ) 長度需與特徵數一樣
# 在這裡特徵為 [x0,sepal_length,petal length (cm)]
# x0 永遠為 1
w = np.array([0.,0.,0.])
error = 1 # 錯誤次數
iterator = 0 # 迭代計數器
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
        
        # np.dot 會把兩個 np.array 的所有相對應的值相乘後全部加起來
        result = activation(np.dot(w,x))

        if result != y:
            error += 1
            iterator += 1
            w += y*x
    print(error,w,y,result,np.dot(w,x))

# 以下為視覺化

x_decision_boundary = np.linspace(0,7,2) # 在 0 ~ 7 之間取兩個點

# ax+by+c=0 為一直線 ( 決策邊界, 分割線 )
# by = -ax-c
# y = (-ax-c)/b
# y = -ax/b - c/b
# c = x0*w0, x0 = 1, c = w0
# a -> w1
# b -> w2
# y = -w1*x/w2-w0/w2
# y = (-w1/w2)*x - (w0/w2)
y_decision_boundary = (-w[1]/w[2])*x_decision_boundary-(w[0]/w[2])

print(w)
print(x_decision_boundary)
print(y_decision_boundary)

sns.lmplot('sepal length (cm)','petal length (cm)',iris_data,hue='target',fit_reg=False,)
plt.plot(x_decision_boundary,y_decision_boundary,'r')

plt.show()

print("End")
