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
def quicksort(array,left,right):
    i,j,x = left,right,array[(left+right)/2]
    while True:
        while array[i]<x:
            i+=1
        while array[j]>x:
            j-=1
        if i<=j:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            i+=1
            j-=1
        else:
            break
    if left<j:
        quicksort(array,left,j)
    if right>i:
        quicksort(array,i,right)
if __name__ == '__main__':
    main()
n = input("Enter n")
m = input("Enter m")
array =[]
for i in range(n):
    array.append(input())
quicksort(array,0,n-1)
print array
triplets =0
for i in range(n-2):
    l=i+1
    r=n-1
    while l<r:
        sum = array[i]+array[l]+array[r]
        if sum==m:
            triplets+=1
            break
        elif sum<m:
            l+=1
        else:
            r-=1
print triplets
