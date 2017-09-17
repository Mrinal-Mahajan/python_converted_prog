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

def main():
    pass

if __name__ == '__main__':
    main()
t = input("Enter no. of test casee")
for i in range(t):
    sequence = []
    pos = input("Enter position")
    while True:
        a = input()
        if a==-1:
            break
        sequence.append(a)

    if pos>len(sequence):
        print -1
    else:
        sequence.sort()
        print sequence[pos-1]

