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
a =0

def blocks(n):
    global a
    if n==0:
        return
    if n==1:
        a+=1
        return
    blocks(n-1)
    a+=1
    blocks(n-1)


if __name__ == '__main__':
    main()
n = input("Enter n")
blocks(n)
print a