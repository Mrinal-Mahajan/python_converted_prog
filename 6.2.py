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
class stack:
    def __init__(self):
        self.container = []
    def push(self,number):
        self.container.append(number)
    def pop(self):
        return self.container.pop(self.size-1)
    def size(self):
        return len(self.container)
    def isempty(self):
        return self.size == 0
    def returnnln(self,stack2):
        l = len(stack2.container)
        for i in range(l):
            j=i
            while j>=0:
                if stack2.container[j]>stack2.container[i]:
                    self.container.append(stack2.container[j])
                    break
                else:
                    j-=1
            if i==0 or j==-1:
                self.container.append(-1)




if __name__ == '__main__':
    main()
n = input("Enter size")
question = stack()
for i in range(n):
    question.push(input())
answer = stack()
answer.returnnln(question)
print answer.container