import re

totalSum = 0
newFile = open("Myfile2.txt")
for line in newFile:
    num =  re.findall('[0-9]+', line)
    for number in num:
        totalSum += int(number)
print(totalSum)