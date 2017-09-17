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
class String:
    def __init__(self,str):
        self.str = str
    def add(self,str2):
        self.str+=str2
    def replace(self,old,new):
        s = list(self.str)
        for i in range(len(s)):
            if s[i]==old:
                s[i]=new
        self.str = "".join(s)

if __name__ == '__main__':
    main()
string1 = String(raw_input("Enter string"))
string1.add(raw_input("Enter joined string"))
print string1.str
string1.replace(raw_input("enter old "),raw_input("enter new"))
print string1.str