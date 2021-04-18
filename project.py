import csv
import math
with open("data.csv") as f:
    reader = csv.reader(f)
    fileData = list(reader)
data = fileData[0]
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean
squaredlist = []
for i in data:
    a = int(i) - mean(data)
    a = a**2
    squaredlist.append(a)
sum = 0
for i in squaredlist:
    sum = sum + i
result = sum/len(data) - 1
standarddeviaton = math.sqrt(result)
print(standarddeviaton)