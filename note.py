from datetime import datetime

s = "The youngest pope was 11 years old"
a = "01:00:00"
b = "01:00:00"
c = 'Jan 2, 2023 00:00 AM'
d = 'Jan 3, 2023 00:00 AM'

x = s.split() # string array
print(x[-3] + " " + x[-1] + " " + x[2] + "s")
#11 old popes

z = a.split(':')
print(z[0])
print(z[1])
print(z[2])
print(z[0]+":"+z[1]+":"+z[2])

start_time = "2:13:57"
t1 = datetime.strptime(a, "%H:%M:%S")
t2 = datetime.strptime(start_time, "%H:%M:%S")
t3 = datetime.strptime(c, "%b %d, %Y %H:%M %p")
t4 = datetime.strptime(d, "%b %d, %Y %H:%M %p")

print('Start time:', t1.time())

print(t1.time())
print(t2.time())


delta = t2 - t1

print(delta)
print(a)

print(t3.time())
print(t4.time())

minus = t4 - t3

print(minus)
################################################
from datetime import datetime
import pandas as pd
import numpy as np

#https://www.w3schools.com/python/module_statistics.asp

df = pd.read_excel('mean.xlsx')

#https://www.skytowner.com/explore/python_datetime_strptime_method
t1 = pd.to_datetime(df['Response time elapsed'], format='%H:%M:%S')

t2 = pd.to_datetime(df['Resolved Time'], format='%b %d, %Y %H:%M %p')


print("Rata-rata respon time :", t1.mean())
print("Rata-rata resolve :", t2.mean())


