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
array= []
max =0
for i in range(0,n):
    array.append(raw_input())
for i in range(0,n):
    for j in range(0,n-i):
        sum = array[i]
        for k in range(1,j+1):
            sum+=array[i+k]
        if sum>max:
            max=sum
print max