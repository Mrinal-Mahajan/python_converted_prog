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
T = input("Enter T")
array,result =[],[]
for i in range(T):
    for j in range(10):
        array.append(input(""))
    for k in range(1,4):
            min = 30
            for j in range(10):
                if array[j]<=min:
                    min=array[j]
            if k<=2:
                for j in range(10):
                    if min==array[j]:
                        array[j]=31
                        break
            else:
                for j in range(10):
                    if min==array[j]:
                        result.append(j+1)
                        break
print result
