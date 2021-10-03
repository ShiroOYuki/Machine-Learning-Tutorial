import pandas as pd

data = [
    [87,1,2,3,4], 
    [12,5,6,1,2], 
    [55,4,3,8,7], 
    [16,5,4,8,4]
]
columns = ["i","ii","iii","iv","v"]

df = pd.DataFrame(data,columns=columns)
df_norm = pd.DataFrame(data,columns=columns)
df_std = pd.DataFrame(data,columns=columns)

print("\n\n" + '=-'*20 + "Feature Scaling" + '-='*20 + "\n\n")
print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")
print(df)

# Normalization

df_norm["i"] = (df_norm["i"]-df_norm["i"].min()) / (df_norm["i"].max() - df_norm["i"].min())

print("\n\n" + '-'*20 + "Normalization" + '-'*20 + "\n\n")
print(df_norm)

# Standardization

# .std() : 求標準差
df_std["i"] = (df_std["i"]-df_std["i"].mean())/df_std["i"].std()

print("\n\n" + '-'*20 + "Standardization" + '-'*20 + "\n\n")
print(df_std)
print("df_std['i'].mean()={}\ndf_std['i'].std()={}".format(int(df_std["i"].mean()),df_std["i"].std()))