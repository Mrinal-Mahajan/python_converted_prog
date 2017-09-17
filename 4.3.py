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
def polynomial(array,k,m):
    if m==0:
        return array[0]
    else:
        return array[m] + polynomial(array,k,m-1)*k

if __name__ == '__main__':
    main()
n = input("Enter n")
m = input("Enter m")
k=input("Enter k")
array =[]
for i in range(n+1):
    array.append(input())
print polynomial(array,k,m)