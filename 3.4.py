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
def power(x,y):
    if(y==0):
        return 1
    if y==1:
        return x
    if y%2==0:
        return power(x,y/2)*power(x,y/2)
    else:
        return x*power(x,y/2)*power(x,y/2)
if __name__ == '__main__':
    main()
n = input("Enter n")
x = input("Enter x")
coeff,sum =[0 for i in range(n)],0
for i in range(n,-1,-1):
    coeff.insert(i,input())
    sum+=coeff[i]*power(x,i)
print sum