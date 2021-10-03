# 資料視覺化 ( Data Visualization )

## Matplotlib

### 基礎

* 常跟 pandas、Numpy 做結合

* 主要常用圖表有：
    
    * plt.plot()：折線圖
    
    * plt.bar()：長條圖
    
    * plt.scatter()；散布圖

* 每次要顯示圖片都需要 plt.show()

* 在 Jupyter Notebook 內可以在一開始 import 完後加入 `%matplotlib inline` 來省略之後的 plt.show()

* [完整圖表內容](https://matplotlib.org/stable/gallery/index.html)

### 常用函式

* plt.plot(\<x1>, \[y1], \[line style1], \[x2], \[y2], \[line style2])
    
    > 繪製折線圖  
    > x、y 必須要是長度相同的陣列  
    > line style : str

    * [詳細內容](https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html)

* plt.bar(\<x>, \[y], \[width])

    > 繪製長條圖  
    > x、y 必須要是長度相同的陣列  
    > width 預設為 0.8

    * [詳細內容](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)

* plt.scatter(\<x>, \<y> ,c=\[color])

    > 繪製散布圖  
    > x、y 必須要是長度相同的陣列  
    > color : str  
    > 若要繪製多種不同顏色，就直接打好幾行，然後再一次 plt.show() 出來

    * [詳細內容](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)

    * [其他範例](https://www.delftstack.com/zh-tw/howto/matplotlib/set-color-for-scatterplot-in-matplotlib/)

* plt.show()：顯示圖表

* plt.style.use()：如果懶得慢慢調圖表樣式，可以用這個函式直接套內建 style

    * plt.style.use("default")：恢復預設樣式

    * plt.style.available：顯示可用的 style

### 範例

* [Matplotmat.ipynb](./Matplotmat.ipynb)

---

## Seaborn
