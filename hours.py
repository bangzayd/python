import pandas as pd

df = pd.DataFrame({'datetime': ['20:30:00', '21:30:00']})

# convert to datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# take difference to normalized datetime
df['time'] = df['datetime'] - df['datetime'].dt.normalize()

# calculate mean and format
res = str(df['time'].mean())[-8:]

print(res)
