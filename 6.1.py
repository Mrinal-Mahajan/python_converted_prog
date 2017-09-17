#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     25-09-2016
# Copyright:   (c) DELL 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass
def isbalanced(array):
    temp,i = len(array),0
    while temp!=0:
        temp/=2
        i+=1
    if i==1:
        return True
    else:
        lsum,rsum = 0,0
        for j in range(1,i):
            for k in range(pow(2,j)-1,pow(2,j)+pow(2,j-1)-1):
                lsum+=array[k]
            for k in range(pow(2,j)+pow(2,j-1)-1,pow(2,j+1)-1):
                rsum+=array[k]
        if lsum==rsum:
            return True
        else:
            return False

if __name__ == '__main__':
    main()
n = input("Enter no. of elements")
array =[]
for i in range(n):
    array.append(input())
if isbalanced(array) == True:
    print "Tree is balanced"
else:
    print "Tree is not balanced"