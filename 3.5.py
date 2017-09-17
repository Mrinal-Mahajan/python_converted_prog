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
import sys
def main():
    pass
if __name__ == '__main__':
    main()
string = raw_input("Enter String")
length = len(string)
for j in range(length):
    if string[j]==string[length-j-1]:
        sys.stdout.write(string[j])
        continue
    else:
        if j==0:
            print 0
            break
        else:
            break

