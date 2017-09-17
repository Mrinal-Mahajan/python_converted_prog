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
n = input("Enter n")
num = input("Enter num")
array,diff =[],[]
for i in range(n):
    array.append(input())
    diff.append(abs(array[i]-num))
for j in range(1,6):
    min = 20000
    for i in range(n):
        if diff[i]<=min:
            min = diff[i]
            index =i
    print array[index],
    diff[index]=20001