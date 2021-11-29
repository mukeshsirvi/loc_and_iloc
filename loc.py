import pandas as pd
df=pd.read_csv("Data.csv")
print(df)
print(df.loc[[2]])
print(df.loc[[2,4]])
print(df.loc[[2,4],["Country"]])
print(df.loc[2:,:])
print(df.loc[2:,"Country":"Salary"])



