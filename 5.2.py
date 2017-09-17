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
class matrixtype:
    matrix =[]
    def __init__(self,array):
        self.matrix = array
        self.dim = len(array)



def addition(M1,M2):
        result = [[0 for x in range(M1.dim)]for y in range(M1.dim)]
        for i in range(M1.dim):
            for j in range(M1.dim):
                result[i][j] = M1.matrix[i][j]+M2.matrix[i][j]
        return result


def subtraction(M1,M2):
        result = [[0 for x in range(M1.dim)]for y in range(M1.dim)]
        for i in range(M1.dim):
            for j in range(M1.dim):
                result[i][j] = M1.matrix[i][j]-M2.matrix[i][j]
        return result


def multiplication(M1,M2):
        result = [[0 for x in range(M1.dim)]for y in range(M1.dim)]
        for i in range(M1.dim):
            for j in range(M1.dim):
                for k in range(M1.dim):
                    result[i][j]+= M1.matrix[i][k]*M2.matrix[k][j]
        return result


if __name__ == '__main__':
    main()
    dim = input("Specify dimension")
    array1 =[[input() for x in range(dim)]for y in range(dim)]
    array2 =[[input() for x in range(dim)]for y in range(dim)]
    M1,M2 = matrixtype(array1),matrixtype(array2)
    operation = raw_input("specify operation")
    if operation=='+':
        print addition(M1,M2)
    elif operation=='-':
        print subtraction(M1,M2)
    elif operation=='*':
        print multiplication(M1,M2)
    else:
        print "invalid operation"
