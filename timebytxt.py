import datetime

timeList = []

mysum = datetime.timedelta()
with open(r'times.txt') as timeList:
    for line in timeList:
        (h, m, s) = line.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    mysum += d
print(str(mysum))
