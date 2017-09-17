#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     25-09-2016
# Copyright:   (c) DELL 2016
# Licence:     <your licence>
#-----------------------------------------------------------------------------
def main():
    pass
class student:
    marks = []
    name = None
    def __init__(self,name,marks):
        self.name = name
        self.marks =marks
    def __str__(self):
        return self.name
    def average(self):
        return sum(self.marks)/len(self.marks)
def gettopper(students,subject):
    marks =[]
    for i in range(len(students)):
        marks.append(students[i].marks[subject])
    return students[marks.index(max(marks))].name
if __name__ == '__main__':
    main()
n = input("Enter no. of students")
k = input("Enter no. of subjects")
records = []
for i in range(n):
    name = raw_input("Enter name")
    marks =[]
    for j in range(k):
        marks.append(input())
    record = student(name,marks)
    records.append(record)
    print sum(marks)/k
for i in range(k):
    print gettopper(records,i)
