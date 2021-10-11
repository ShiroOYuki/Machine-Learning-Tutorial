from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap

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

# 抓特徵
x = pd.DataFrame(iris["data"],columns=iris["feature_names"])
print(x)

# 抓應輸出的值
y = pd.DataFrame(iris["target"],columns=["target"])
print(y)

# 合併
iris_data = pd.concat((x,y),axis=1)
print(iris_data)

# 只留兩種資料 ( 原本有 0, 1, 2 三種 )
iris_data = iris_data[(iris_data["target"] == 0)|(iris_data["target"] == 1)]
print(iris_data)

# columns :
# sepal length (cm) 
# sepal width (cm) 
# petal length (cm)
# petal width (cm) 
# target

# 只留兩種特徵和應輸出的值
iris_data = iris_data[['sepal length (cm)','petal width (cm)','target']]
print(iris_data)

# 把資料分為 "訓練用" 跟 "測試用"
# 忘記語法可以看相同資料夾下的 train_test_split_EX.py
# 這裡一定要加 random_state，不然 x 跟 y 的資料會是不同行
x_train,x_test=train_test_split(iris_data[['sepal length (cm)','petal width (cm)']],test_size=0.3,random_state=0)
y_train,y_test=train_test_split(iris_data[['target']],test_size=0.3,random_state=0)
print(len(x_train),len(x_test),len(y_train),len(y_test))

# 使用 Logistic Regression 前須做 Feature Scaling，這裡用 Standardization ( 標準化 )
# 可用 Ch0 寫的方法，或直接套函式
# 這裡是直接套函式
sc = StandardScaler()
sc.fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

print(x_train)
print(x_train_std)
print(x_test)
print(x_test_std)

# Logistic Regression
lr = LogisticRegression()
lr.fit(x_train_std,y_train['target'].values)

# 若 print 出來完全一樣，代表預測完全命中
print(lr.predict(x_test_std))# 預測
print(y_test['target'].values)# 實際答案
error = 0
for i,v in enumerate(lr.predict(x_test_std)):
    if v != y_test['target'].values[i]:
        error += 1

print(f"Error predict : {error}\n")

# 預測機率
print(lr.predict_proba(x_test_std))

print(lr.coef_)# w1、w2
print(lr.intercept_)# w0

w0 = lr.intercept_
w = np.concatenate((w0,lr.coef_[0]))
print(w)

# visualization
# 這次的視覺化是畫出區塊，間接顯示出決策邊界，而不是直接畫決策邊界

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    # X[:, 0] : sepal length (cm) (Std)
    # X[:, 1] : petal width (cm) (Std)
    # -1、+1 是為了留空 ( 不然最小和最大的兩點會直接貼著圖片的框框，很難看 )
    print(X[:, 0].min() - 1, X[:, 0].max() + 1)
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    # np.arange(x1_min, x1_max, resolution) : 
    # 在 x1_min、x1_max 之間以 resolution 為等差級數取值
    # xx1 代表在 sepal length (cm) (Std) 的最小值與最大值內，每 0.02 取一個點 ( x 軸 )
    # xx2 代表在 petal width (cm) (Std) 的最小值與最大值內，每 0.02 取一個點 ( y 軸 )
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    # classifier = lr
    # np.ravel() : 把多維陣列拉直成一維陣列
    xx = np.array([xx1.ravel(), xx2.ravel()])
    print(xx)

    # 把範圍內的所有點 ( 每0.02取一個點 )全部重新預測，並依照預測結果上色
    Z = classifier.predict(xx.T)
    Z = Z.reshape(xx1.shape)
    print(Z)
    
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)

    # np.unique() : 去除重複數字並排序
    # 在這裡是要把每一筆資料的 target 變成 (0,1) ( 原本有很多 0、1 )
    print(y)
    print(np.unique(y))
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.6, 
                    c=cmap(idx),
                    edgecolor='black',
                    marker=markers[idx], 
                    label=cl)

    # highlight test samples
    if test_idx:
        # plot all samples
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    c='yellow',
                    alpha=1.0,
                    edgecolor='black',
                    linewidths=1,
                    marker='o',
                    s=55, label='test set')
plot_decision_regions(x_train_std, y_train['target'].values, classifier=lr)
plt.xlabel('sepal length (cm) [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()