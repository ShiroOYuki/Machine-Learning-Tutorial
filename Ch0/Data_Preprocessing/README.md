# 資料預處理 ( Data Preprocessing )

## Missing data
> 用於資料有缺失時

* 常見的處理方式有兩種：
    
    1. 丟棄 ( 用在資料量夠多時 )
    
    2. 補值

### 丟棄

> 可以使用 pandas 的 `.dropna([Options])`
* Options：
    
    * 為空：刪掉有空值 ( NAN, null ) 的整個橫排
    
    * how="all"：整橫排都是空值才刪掉
    
    * subset=[\<column name1, name2...>]：column name 直排有空值才刪掉該橫排，其餘不理

### 補值

> 可以使用 pandas 的 `.fillna([Options])`
* Options：

    * num：把空值補一個固定數字
    
    * DataFrame.mean()：補平均值
    
    * DataFrame.mode()[0]：補眾數 ( 出現最多次的數字 )

### 範例

* [Missing_Data.py](./Missing_Data.py)

---

## One-hot encoding
> 只適合用在資料特徵少的時候，否則會造成維數災難

### 有序資料
> 如衣服大小 XS S M L XL 可以變成 1 2 3 4 5 

* 可以用 mapping 的方式來改值：`DataFrame[\<column name>].map(<dict>)`
    >```=
    > dict = {  
    >   "XS":1,  
    >   "S":2,
    >   "M":3,
    >   "L":4,
    >   "XL":5,
    >   }  
    >```

### 無序資料
> 這裡就需要用到 One-hot encoding 了  
> 由於是無序的資料，因此需要讓資料值總和相同，才不會影響到運算結果  
> 例如性別：
>
>![](../../Static/Image/Ch0/One-hot-encoding.png)

* 可以用 pandas.get_dummies(DataFrame[\<column name>],[Options])
    * Options：
        * prefix = \<str>：在創出來的欄位加上前綴詞

### 範例

* [One-hot-encoding.py](./One-hot-encoding.py)

---

## Feature Scaling

> 假設特徵 1 ( $\theta_1$ ) 範圍為 1~5，特徵 2 ( $\theta_2$ ) 範圍為 0~2000 時 ( 範圍相差太大時 )，則呈現出來的特徵會是像橢圓形，比較難利用梯度下降來找到圓心，因此需要做 Feature Scaling 來讓他接近一個圓  
> ![](../../Static/Image/Ch0/Feature-scaling.png)

* 常見的 Feature Scaling 演算法有兩種：
    
    1. 歸一化 ( Normalization )
    
    2. 標準化 ( Standardization )

### 歸一化 ( Normalization )

* 最常見的 Normalization 為 0~1 區間縮放，最大值變為 1，最小值變為 0，中間值做等比例縮放：
$$
x_{norm} = \frac{x^{(i)}-x_{min}}{x_{max}-x_{min}}
$$
> $x_{norm}$：$x$ ( Normal )，代表經過 Normalization 後計算出來的值

### 標準化 ( Standardization )
$$
x^{(i)}_{std} = \frac{x^{(i)}-\mu_x}{\sigma_x}
$$
> $\sigma$ ( 讀作 sigma )：標準差，定義為 **"與平均數的平均距離( 平均誤差 )"**，可以用 DataFrame.std() 來取得  
> $\mu$：平均數  
* 經過 Standardization 後的資料平均值會為 0，標準差為 1，且符合常態分布
* 可使離群值 ( Outlier ) 的影響程度大大降低

### 範例

* [Feature_Scaling.py](./Feature_Scaling.py)

---

## 參考資料

* [資料分析-機器學習 2-4 -- Yeh James](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-4%E8%AC%9B-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-missing-data-one-hot-encoding-feature-scaling-3b70a7839b4a)