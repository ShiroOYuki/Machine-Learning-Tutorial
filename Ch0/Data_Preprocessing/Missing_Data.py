import pandas as pd

l = [[1,2,3,4,None],[2,2,4,None,5],[8,8,9,8,1],[None,2,3,4,4],[None,None,None,None,None]]
df = pd.DataFrame(l,columns=["i","ii","iii","iv","v"])

print("\n\n" + '=-'*20 + "dropna" + '-='*20 + "\n\n")

print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")
print(df)

print("\n\n" + '-'*20 + ".dropna()" + '-'*20 + "\n\n")
print(df.dropna())

print("\n\n" + '-'*20 + ".dropna(how='all')" + '-'*20 + "\n\n")
print(df.dropna(how="all"))

print("\n\n" + '-'*20 + ".dropna(subset=['i'])" + '-'*20 + "\n\n")
print(df.dropna(subset=["i"]))

print("\n\n" + '=-'*20 + "fillna" + '-='*20 + "\n\n")

print("\n\n" + '-'*20 + ".fillna(0)" + '-'*20 + "\n\n")
df3 = df2 = df
print(df.fillna(0))

print("\n\n" + '-'*20 + ".fillna(df['iv'].mean())" + '-'*20 + "\n\n")
df2["iv"] = df["iv"].fillna(df["iv"].mean())
print(df2)

print("\n\n" + '-'*20 + ".fillna(df['ii'].mode()[0])" + '-'*20 + "\n\n")
df2["ii"] = df["ii"].fillna(df["ii"].mode()[0])
print(df2)