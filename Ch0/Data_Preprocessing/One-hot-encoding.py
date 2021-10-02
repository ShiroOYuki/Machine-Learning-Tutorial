import pandas as pd

l = [
    ["red","M",100],
    ["green","S",90],
    ["blue","L",110]
]
df = pd.DataFrame(l)
df.columns = ["color","size","price"]

print("\n\n" + '=-'*20 + "Mapping" + '-='*20 + "\n\n")

print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")
print(df)

mapping = {
    "S":1,
    "M":2,
    "L":3
}

print("\n\n" + '=-'*20 + "One Hot Encoding" + '-='*20 + "\n\n")

print("\n\n" + '-'*20 + "Original" + '-'*20 + "\n\n")
df["size"] = df["size"].map(mapping)
print(df)

print("\n\n" + '-'*20 + "pd.get_dummies(df['color'],prefix = 'color')" + '-'*20 + "\n\n")
color_df = pd.get_dummies(df["color"],prefix = "color")
print(color_df)

print("\n\n" + '-'*20 + "pd.concat([color_df,df],1)" + '-'*20 + "\n\n")
df = pd.concat([color_df,df],1)
df = df.drop("color",1)
print(df)