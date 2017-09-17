#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     24-09-2016
# Copyright:   (c) DELL 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
N = input("Enter N")
k = input("Enter k")
array =[]
for i in range(N):
    array.append(input())
for i in range(k):
    min = array[i+1]
    index = i+1
    for j in range(i+2,N):
        if array[j]<=min:
            min = array[j]
            index =j
    temp = array[i]
    array[i]=array[index]
    array[index]=temp
print array