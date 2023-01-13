import datetime

timeList = ['0:00:00', '0:00:15', '9:30:56']
mysum = datetime.timedelta()
for i in timeList:
    (h, m, s) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    mysum += d
print(str(mysum))
