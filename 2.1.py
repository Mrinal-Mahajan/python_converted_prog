#-------------------------------------------------------------------------------
# Name:        module3
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
    m = input("Enter no. of rows")
    n = input("Enter no. of columns")
    Matrix = [[0 for x in range(n)]for y in range(m)];
    for x in range(m):
        for y in range(n):
            Matrix[x][y] = input()

    left,right,top,bottom = 0,n-1,0,m-1
    while True:
        for j in range(left,right+1):
            print Matrix[top][j]
        top = top+1
        for i in range(top,bottom+1):
            print Matrix[i][right]
        right-=1
        for j in range(right,left-1,-1):
            print Matrix[bottom][j]
        bottom-=1
        for i in range(bottom,top-1,-1):
            print Matrix[i][left]
        left+=1
        if left>right or top>bottom:
            break




