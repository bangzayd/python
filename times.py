from datetime import datetime
data = []

with open(r'times.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        data.extend(rowdata)

print(sum(data)/len(data))




