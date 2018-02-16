# Script written by Cyron Completo

import csv
import random

reportStudents = []
critiqueStudents = []

with open('report-students.csv', 'rb') as csvfile:
  fileReader = csv.reader(csvfile, delimiter='"', quotechar='|')
  for row in fileReader:
    for entry in row:
      if entry != '':
        reportStudents.append(entry)

with open('critique-students.csv', 'rb') as csvfile:
  fileReader = csv.reader(csvfile, delimiter='"', quotechar='|')
  for row in fileReader:
    for entry in row:
      if entry != '':
        critiqueStudents.append(entry)

reportTemp = reportStudents
critiqueTemp = []
resultArr = []
for i in range(len(critiqueStudents)):
  critiqueTemp.append(2)

def foo():
  listPeople = []
  for i in range(len(reportStudents)):
    reportStudent = reportStudents[i]
    reportTemp[i] = ""
    x = 0
    y = 2
    z = 30
    a = 0
    while ((x == i or y == i or x == y or critiqueTemp[x] == 0 or critiqueTemp[y] == 0) and a <= z) :
      x = random.randint(0, len(reportStudents)-1)
      y = random.randint(0, len(reportStudents)-1)
      a += 1
    critiqueStudentOne = critiqueStudents[x]
    critiqueTemp[x] -= 1
    critiqueStudentTwo = critiqueStudents[y]
    critiqueTemp[y] -= 1
    if a == z:
      break
    else:
      listPeople.append({reportStudent: [critiqueStudentOne, critiqueStudentTwo]})
  return listPeople

resultArr = foo()

with open('results.csv', 'wb') as csvfile:
  resultsWriter = csv.writer(csvfile, delimiter=',')
  for dicts in resultArr:
    print(dicts)
    for key, value in dicts.items():
      resultsWriter.writerow([key, value[0], value[1]])
      print(value[0])
print("done")