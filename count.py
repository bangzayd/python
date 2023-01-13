import pandas as pd
import numpy as np
df = pd.read_excel('data.xlsx')
print("Sum: ",df["a"].sum()) 
print("Mean: ",df["a"].mean())
print("Maximum: ",df["a"].max())
print("Minimum: ",df["a"].min()) 