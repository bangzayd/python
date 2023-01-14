from datetime import datetime
import pandas as pd
import numpy as np
df = pd.read_excel('a.xlsx')

print(df["a"]) 
print(df["b"])

t1 = pd.to_datetime(df['b'], format='%H:%M:%S')
print(t1)

t2 = pd.to_datetime(df['c'], format='%H:%M:%S')
print(t2)

delta = t2 - t1

print(delta)