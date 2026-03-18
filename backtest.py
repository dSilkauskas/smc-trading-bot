print("Rows in CSV:", len(df))
print(df.head())
print(df.tail())
exit()
import pandas as pd

# LOAD DATA
df = pd.read_csv("nq.csv")

# BASIC CHECKS
print("Rows:", len(df))
print(df.head())
print(df.tail())
















