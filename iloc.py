import pandas as pd
df=pd.read_csv("Data.csv")
print(df)
print(df.iloc[4:6])
print(df.iloc[4:6,0:2])
