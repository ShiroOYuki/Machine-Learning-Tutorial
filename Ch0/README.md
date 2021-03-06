# Ch0. 資料分析

## 獲取資料集
### 資料集來源
* [Sklearn 內建 Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html)

* [Kaggle Dataset](https://www.kaggle.com/datasets)

* Google map API

### 範例

* [Get_Iris.py](./Get_Data/Get_Iris.py)

* [Get_Iris.ipynb](./Get_Data/Get_Iris.ipynb)

---

## [Pandas 基礎](./Pandas_Example/README.md)

### 介紹內容

* 欄位 ( Series )

* 表格 ( DataFrame )

* 資料選取 ( Selection )

* 資料分群 ( Grouping )

### 範例

* [Example.py](./Pandas_Example/Example.py)

---

## [資料預處理 ( Data Preprocessing )](./Data_Preprocessing/README.md)

### 介紹內容
    
* 缺失值的處理 **( Missing data )**

* 類別資料的處理（有序、無序）**( One-hot encoding )**

* 資料特徵縮放 **( Feature Scaling )**

> 除了這些以外還有很多其他的進階方法

### 範例

* [Missing_Data.py](./Data_Preprocessing/Missing_Data.py)

* [One-hot-encoding.py](./Data_Preprocessing/One-hot-encoding.py)

* [Feature_Scaling.py](./Data_Preprocessing/Feature_Scaling.py)

---

## [資料視覺化 ( Data Visualization )](./Data_Visualization/README.md)

* 這裡主要介紹以下兩種：
    
    1. Matplotlib ( 簡稱 plt )
    
    2. Seaborn ( 簡稱 sns )

### Matplotlib

* 優點
    
    * 這個庫發展了很久，基本上沒有他畫不出來的圖表 ( 只有你寫不出來 \_(┐「ε:)\_ )
    
    * 有很多的教學文章或是範例可參考

* 缺點
    
    * 指令有夠複雜 ( ´•ω•` )

### Seaborn

* 優點

    * 指令簡單 (｡･∀･)ﾉﾞ
    
    * 圖表還蠻漂亮的 (✿゜▽゜)♪

* 缺點

    * 比起 Matplotlib 來說，能畫的圖比較少，但可以跟 Matplotlib 交互使用

### 範例

* [Matplotlib.ipynb](./Data_Visualization/Matplotlib.ipynb)

* [Seaborn.ipynb](./Data_Visualization/Seaborn.ipynb)

# 參考資料

* [資料分析-機器學習 2-1 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-1%E8%AC%9B-%E5%A6%82%E4%BD%95%E7%8D%B2%E5%8F%96%E8%B3%87%E6%96%99-sklearn%E5%85%A7%E5%BB%BA%E8%B3%87%E6%96%99%E9%9B%86-baa8f027ed7b)

* [資料分析-機器學習 2-3 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-3%E8%AC%9B-pandas-%E5%9F%BA%E6%9C%ACfunction%E4%BB%8B%E7%B4%B9-series-dataframe-selection-grouping-447a3fa90b60)

* [資料分析-機器學習 2-4 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-4%E8%AC%9B-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-missing-data-one-hot-encoding-feature-scaling-3b70a7839b4a)

* [資料分析-機器學習 2-5 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f)