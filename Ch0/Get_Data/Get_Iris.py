# From scikit-learn
from sklearn import datasets

# Get Iris dataset
iris = datasets.load_iris()
print(iris)

print("\n\n" + '=-'*40 + "\n\n")

# Get Dataset's keys
keys = iris.keys()
print(iris.keys())
# key = dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

for key in keys:
    print("\n\n" + '-'*20 + key + '-'*20 + "\n\n")
    print(iris[key])

print("\n\n" + '=-'*40 + "\n\n")

# 建個表格方便看
import pandas as pd

print('-'*20 + "x" + '-'*20 + "\n\n")
x = pd.DataFrame(iris["data"],columns=iris["feature_names"])
print(x)

print("\n\n" + '-'*20 + "y" + '-'*20 + "\n\n")
y = pd.DataFrame(iris["target"],columns = ["target_names"])
print(y)

print("\n\n" + '-'*20 + "data" + '-'*20 + "\n\n")
data = pd.concat([x,y],axis=1)
print(data)