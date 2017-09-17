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
s1 = raw_input("Enter String1")
s2 = raw_input("Enter String2")
len1,len2 = len(s1),len(s2)
if len1==len2 :
    for k in range(0,len1):
        n1,n2 = 0,0
        for i in range(0,len1):
            if s1[k] == s1[i]:
                n1+=1
            if s1[k] == s2[i]:
                n2+=1
        if n1==n2:
            continue
        else:
            break
    if k==len1-1:
        print "yes"
    else:
        print "no"
else:
    print "no"


