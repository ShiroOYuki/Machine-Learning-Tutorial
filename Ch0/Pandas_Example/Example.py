from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

print("\n\n" + '=-'*20 + "Series" + '-='*20 + "\n\n")
# Series

# np.nan : 空值
s = pd.Series([9,4,8,7,np.nan,"Yuki"])
s2 = pd.Series([9,4,8,7,np.nan,"Yuki"],index=["a","b","c","d","e","f"])

print('-'*20 + "Original" + '-'*20 + "\n\n")

print(s)

print("\n\n" + '-'*20 + " + index" + '-'*20 + "\n\n")

print(s2)

print("\n\n" + '=-'*20 + "DataFrame" + '-='*20 + "\n\n")

# DataFrame

# np.random.randn() : 隨機生成符合 "標準常態分佈" 的亂數
# 標準常態分佈圖 : https://www.ruanyifeng.com/blogimg/asset/2017/bg2017073006.jpg
# (6,4) : 生成高為 6，寬為 4 共 24 個數值
df = pd.DataFrame(np.random.randn(6,4))
df2 = pd.DataFrame(np.random.randn(6,4),index=["a","b","c","d","e","f"])
df3 = pd.DataFrame(np.random.randn(6,4),index=["a","b","c","d","e","f"],columns=["i","ii","iii","iv"])

print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")

print(df)

print("\n\n" + '-'*20 + " + index" + '-'*20 + "\n\n")

print(df2)

print("\n\n" + '-'*20 + " + index + columns" + '-'*20 + "\n\n")

print(df3)

print("\n\n" + '='*20 + "Def" + '='*20 + "\n\n")

print("\n\n" + '-'*20 + ".columns" + '-'*20 + "\n\n")

print(df3.columns)

print("\n\n" + '-'*20 + ".head(5)" + '-'*20 + "\n\n")

print(df3.head(5))

print("\n\n" + '-'*20 + ".tail(5)" + '-'*20 + "\n\n")

print(df3.tail(5))

print("\n\n" + '-'*20 + ".info()" + '-'*20 + "\n\n")

print(df3.info())

print("\n\n" + '-'*20 + ".describe()" + '-'*20 + "\n\n")

print(df3.describe())

print("\n\n" + '-'*20 + ".sort_values(by='iv')" + '-'*20 + "\n\n")

print(df3.sort_values(by="iv"))

print("\n\n" + '=-'*20 + "Selection" + '-='*20 + "\n\n")

# Selection

print("\n\n" + '-'*20 + "['iii']" + '-'*20 + "\n\n")

print(df3["iii"])

print("\n\n" + '-'*20 + "[['ii','iv']]" + '-'*20 + "\n\n")

print(df3[["ii","iv"]])

print("\n\n" + '-'*20 + "['iii'].head(2)" + '-'*20 + "\n\n")

print(df3["iii"].head(2))

print("\n\n" + '-'*20 + "['iii'].tail(2)" + '-'*20 + "\n\n")

print(df3["iii"].tail(2))

print("\n\n" + '-'*20 + "[1:3]" + '-'*20 + "\n\n")

print(df3[1:3])

print("\n\n" + '-'*20 + "[1:3][['i','iii']]" + '-'*20 + "\n\n")

print(df3[1:3][["i","iii"]])

print("\n\n" + '-'*20 + ".loc['a':'c']" + '-'*20 + "\n\n")

print(df3.loc["a":"c"])

print("\n\n" + '-'*20 + ".loc['a':'c',['i','iii']]" + '-'*20 + "\n\n")

print(df3.loc["a":"c",["i","iii"]])

print("\n\n" + '-'*20 + "[df3['i'] > 0]" + '-'*20 + "\n\n")

print(df3[df3["i"] > 0])

l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df4 = pd.DataFrame(l, columns=["a", "b", "c"])

print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")

print(df4)

print("\n\n" + '-'*20 + ".groupby(by='b').sum()" + '-'*20 + "\n\n")

print(df4.groupby(by="b").sum())

print("\n\n" + '-'*20 + ".groupby(by='b').mean()" + '-'*20 + "\n\n")

print(df4.groupby(by="b").mean())

print("\n\n" + '-'*20 + ".groupby(by='b',dropna=False).sum()" + '-'*20 + "\n\n")

print(df4.groupby(by="b",dropna=False).sum())

print("\n\n" + '-'*20 + ".groupby(by=['a','b']).sum()" + '-'*20 + "\n\n")

print(df4.groupby(by=["a","b"]).sum())