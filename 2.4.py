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
string = raw_input("Enter string")
n = len(string)
for i in range(0,n):
    if string[i]>='a' and string[i]<='z':
        k=0
        for j in range(0,i):
            if string[j]=='(':
                k+=1
            if string[j]==')':
                k-=1
        print k