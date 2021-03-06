# 前置條件

## 基礎觀念

* 神經網路模型 ( Neural Network, NN ) 

    ![](./Static/Image/Ch1/NN.png)

* 演算法地圖

    ![](Static/Image/Ch1/Algorithm_cheat_sheet.png)

* 機器學習分為：
    
    * 監督式學習(supervised learning)
    
    * 非監督式學習(unsupervised learning)
    
    * 半監督式學習(semi-supervised learning)
    
    * 增強式學習(reinforcement learning)

* 深度學習 ?：

    * 深度學習原本是機器學習的一部分，但後來被另外獨立出來

    * 由於在類神經網絡隱藏層的地方有非常多層，因此得名"深度"學習

* 通常在機器學習領域內：
   
    * $x$ 代表：特徵 ( feature )、資料
    
    * $y$ 代表：目標 ( target )、結果

---

## 函式庫

* Numpy >= 1.17.4

* Scipy >= 1.3.1

* scikit-learn >= 0.22.0
    > import 時的名稱為 sklearn

* Matplotlib >=3.1.0

* Seaborn

* pandas >= 0.25.3

# [Ch0. 資料分析](./Ch0/README.md)

## 獲取資料集
### 資料集來源
* [Sklearn 內建 Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html)

* [Kaggle Dataset](https://www.kaggle.com/datasets)

### 範例

* [Get_Iris.py](./Ch0/Get_Data/Get_Iris.py)

* [Get_Iris.ipynb](./Ch0/Get_Data/Get_Iris.ipynb)

---

## [Pandas 基礎](./Ch0/Pandas_Example/README.md)
### Function

* 欄位 ( Series )

* 表格 ( DataFrame )

* 資料選取 ( Selection )

* 資料分群 ( Grouping )

### 範例

* [Example.py](./Ch0/Pandas_Example/Example.py)

---

##  [資料預處理 ( Data Preprocessing )](./Ch0/Data_Preprocessing/README.md)

* Missing data

* One-hot encoding

* Feature Scaling

### 範例

* [Missing_Data.py](./Ch0/Data_Preprocessing/Missing_Data.py)

* [One-hot-encoding.py](./Ch0/Data_Preprocessing/One-hot-encoding.py)

* [Feature_Scaling.py](./Ch0/Data_Preprocessing/Feature_Scaling.py)

---

## [資料視覺化 ( Data Visualization )](./Ch0/Data_Visualization/README.md)

* 這裡主要介紹以下兩種：
    
    1. Matplotlib ( 簡稱 plt )
    
    2. Seaborn ( 簡稱 sns )

### 範例

* [Matplotlib.ipynb](./Ch0/Data_Visualization/Matplotlib.ipynb)

* [Seaborn.ipynb](./Ch0/Data_Visualization/Seaborn.ipynb)

# [Ch1. 感知器 與 適應線性神經元](./Ch1/README.md)
## 演算法

* 感知器 ( Perceptron, PLA )

* 適應線性神經元 ( Adaptive linear neurons )

---

## 數據集

* 鳶尾花數據集 ( Iris Dataset )

---

## 套件

* pandas

* Numpy

* matplotlib

---

## README

* [感知器](./Ch1/Perceptron/README.md)

* [適應線性神經元](./Ch1/Adaptive_linear_neurons/README.md)

---

## 範例

* 感知器：[Perceptron.py](./Ch1/Perceptron/Perceptron.py)

* 適應線性神經元：[Adaptive_linear_neurons.py](./Ch1/Adaptive_linear_neurons/Adaptive_linear_neurons.py)

# 參考資料 

* Python 機器學習(上) -- 博碩出版

* [資料分析-機器學習 2-1 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-1%E8%AC%9B-%E5%A6%82%E4%BD%95%E7%8D%B2%E5%8F%96%E8%B3%87%E6%96%99-sklearn%E5%85%A7%E5%BB%BA%E8%B3%87%E6%96%99%E9%9B%86-baa8f027ed7b)

* [資料分析-機器學習 2-3 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-3%E8%AC%9B-pandas-%E5%9F%BA%E6%9C%ACfunction%E4%BB%8B%E7%B4%B9-series-dataframe-selection-grouping-447a3fa90b60)

* [資料分析-機器學習 2-4 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-4%E8%AC%9B-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-missing-data-one-hot-encoding-feature-scaling-3b70a7839b4a)

* [資料分析-機器學習 2-5 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f)
