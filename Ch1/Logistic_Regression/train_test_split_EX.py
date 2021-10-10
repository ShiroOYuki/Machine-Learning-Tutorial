from sklearn.model_selection import train_test_split

data = [0,1,2,3,4,5,6,7,8,9]

a,b = train_test_split(data)
# train_test_split() 會將 data 切割成兩筆不同資料
# 也可以寫入 test_size = 0.4 來讓他以 40% 的比例分割 ( 也可以是其他數字，預設 0.3 )
# 也可以寫入 random_state = 0 來用種子隨機產生 ( 也可以是其他數字 )
# 同一種子產出的結果每次都會相同
# 不加代表每次都隨機產生
print(a)
print(b)

# 或一次分割多個陣列
data0 = [0,1,2,3,4,5,6,7,8,9]
data1 = [10,11,12,13,14,15,16,17,18,19]

a,b,c,d = train_test_split(data0,data1,test_size=0.4)
print(a)
print(b)
print(c)
print(d)