n = int(input())
studentsDict = {}
for _ in range(n):
    marksList = list()
    line = input().split()
    name = line[0]
    for marks in line[1:]: 
        marksList.append(marks)
    studentsDict[name] = marksList
query = input()
intMarksList = []
for marks in studentsDict[query]:
    intMarksList.append(float(marks))
average = float(sum(intMarksList)/len(intMarksList))
print ('%.2f'%average)