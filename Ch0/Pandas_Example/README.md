# Pandas Function
## 資料集

* Iris Dataset

---

## 函式庫

* scikit-learn

* pandas

* Numpy

---

## 基礎
> 通常 pandas 會跟 Numpy 同時使用
* pandas 主要分為三大資料結構：

    1. 欄位 ( Series )
    
    2. 表格 ( DataFrame )
    
    3. 三維表格 ( Panel ) -> 不常用，跳過 (ﾉ)`ω´(ヾ)

---

## 欄位 ( Series )

* 語法：
    
    ```=
    s = pd.Series(<data>, [index])
    ```
    > data：資料  
    > index：欄位 ( 直 ) 

---

## 表格 ( DataFrame )

* 語法：
    
    ```=
    df = pd.DataFrame(<data>, [index], [columns])
    ```
    > data：資料  
    > index：欄位 ( 直 )  
    > columns：欄位 ( 橫 )

* 常用函式：

    * .columns：顯示所有欄位名稱

    * .info()：
        
        * 資料筆數
        
        * 資料型態
        
        * 有無空值 ( null )
        
        * 記憶體使用量
    
    * .describe()

        * 資料平均值
        
        * 資料分布情形 ( min、25%、50%、75%、max)
        
        * 有無資料傾斜 ( Skew )

    * .head( \<num>:int )：顯示前 num 筆資料

    * .tail( \<num>:int )：顯示後 num 筆資料

    * .sort_values( by=\<column name>:str )：依照指定欄位內的資料來做排序

---

## 資料選取 ( Selection )

* 選取欄位：DataFrame[\<column name>]
    > 選取多個欄位：
    DataFrame[[\<column name1, name2, name3...>]]  
    >> 要注意多個欄位是用 [] 再框一層

* .head( \<num>:int )：選取前 num 筆資料

* .tail( \<num>:int )：選取後 num 筆資料

* DataFrame[\<head:int>:\<tail:int>]：選取第 head 行到第 tail 行
    > 若要再加入選擇欄位，則要接在後面：  
    > DataFrame[\<head:int>:\<tail:int>][[\<column name1, name2, name3...>]]

* .loc[\<head>:\<tail>]：選取 head 行到 tail ( 包含 tail ) 行
    > 若要再加入選擇欄位，就直接放在 .loc[]內：  
    > DataFrame.loc[\<head>:\<tail>,[\<column name1, name2, name3...>]]
    >> 注意 head 跟 tail 要符合 index name

* 資料篩選：
    > 直接放 [] 內就好，例如：  
    > DataFrame[DataFrame[\<column name>] > \<num>]  
    > 選出在該 DataFrame 中欄位 column name 的數值 > num 的所有行

---

## 資料分群 ( Grouping )

* .groupby(by=\<key>).sum()：
    * 把所有 key ( 行或列 ) 相同的值全部相加

* .groupby(by=\<key>).mean()：
    * 把所有 key ( 行或列 ) 相同的值全部取平均值

> 以上的 \<key> 也可以替換成 [\<key1,key2...>] 來更精準的分群  
> 可以在 .groupby() 內加入 dropna=\<True/False> 來決定是否忽略 NAN 項

---

## 範例

* [Example.py](./Example.py)

---

## 參考資料

* https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-3%E8%AC%9B-pandas-%E5%9F%BA%E6%9C%ACfunction%E4%BB%8B%E7%B4%B9-series-dataframe-selection-grouping-447a3fa90b60
