from datetime import datetime
import pandas as pd
import numpy as np
df = pd.read_excel('convert.xlsx')


t1 = pd.to_datetime(df['b'], format='%H:%M:%S')
t2 = pd.to_datetime(df['c'], format='%H:%M:%S')

delta = t2 - t1

print(delta)

t3 = pd.to_datetime(df['x'], format='%H:%M:%S')
t4 = pd.to_datetime(df['y'], format='%H:%M:%S')

z = t4 - t3
print(z)

print(t1.mean())
print(t2.mean())
