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
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
def permutation(a,b):
    if(a>=b):
        return factorial(a)/factorial(a-b)
    else:
        return 0
def combination(c,d):
    return permutation(c,d)/factorial(d)
def main():
    pass

if __name__ == '__main__':
    main()
list=[]
for i in range(4):
    a=input("first number")
    list.append(a)
#a = input("enter a")
#b = input("enter b")
#c = input("enter c")
#d = input("enter d")
print combination(list[0],list[1])-permutation(list[2],list[3])