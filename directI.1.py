#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     01-10-2016
# Copyright:   (c) DELL 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
t = input()
answer = []
for i in range(t):
    str1 = raw_input()
    n1 = len(str1)
    str2 = raw_input()
    n2 = len(str2)
    int1 = int(str1)
    int2 = int(str2)
    list1 =[]
    list2 = []
    while(int1 != 0):
        list1.append(int1 % 10)
        int1/=10
    while(int2 != 0):
        list2.append(int2 % 10)
        int2/=10
    cost = 0
    count1 = [0 for x in range(10)]
    count2 = [0 for x in range(10)]
    for i in range(n1):
        count1[list1[i]]+=1
    for i in range(n2):
        count2[list2[i]]+=1
    cost = 0
    for i in range(10):
        cost+=abs(count1[i]-count2[i])*i
        if count1[i]>count2[i]:
            for j in range(abs(count1[i]-count2[i])):
                list1.remove(i)
        if count2[i]>count1[i]:
            for j in range(abs(count1[i]-count2[i])):
                list2.remove(i)
    n1 = len(list1)
    index1 = index2 =0
    while index1<n1 and index2<n1:
        if list1[index1]>list2[index2]:
            sum =0
            for j in range(index2,n1,1):
                if list2[j]!=list1[index1]:
                    sum+=list2[j]
                else:
                    break
            if sum<list1[index1]:
                cost+=sum
                index2 = j
            else:
                cost+=list1[index1]
                index1+=1
        elif list2[index2]>list1[index1]:
            sum =0
            for j in range(index1,n1,1):
                if list2[index2]!=list1[j]:
                    sum+=list1[j]
                else:
                    break
            if sum<list2[index2]:
                cost+=sum
                index1 = j
            else:
                cost+=list2[index2]
                index2+=1
        else:
            index1+=1
            index2+=1


    answer.append(cost)

for i in range(t):
    print answer[i]
