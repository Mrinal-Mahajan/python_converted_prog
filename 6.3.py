#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     26-09-2016
# Copyright:   (c) DELL 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
class Treenode:
    def __init__(self):
        self.value = None
        self.lchild = None
        self.rchild = None
    def setvalue(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None
    def set_to_none(self):
        self.value = None
        self.lchild= None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = Treenode()
    def insert(self,value,node):
        if node.value is None:
            node.setvalue(value)
        else:
            if value>node.value:
                if node.rchild is not None:
                    self.insert(value,node.rchild)
                else:
                    node.rchild = Treenode()
                    node.rchild.setvalue(value)
            elif value<node.value:
                if node.lchild is not None:
                    self.insert(value,node.lchild)
                else:
                    node.lchild = Treenode()
                    node.lchild.setvalue(value)
            else:
                print "value already exist"
    def remove(self,value,node):
        if node == None:
            print "Value isn't found"
        else:
            if value>node.value:
                self.remove(value,node.rchild)
            elif value < node.value:
                self.remove(value,node.lchild)
            else:
                prev = node
                t = node.lchild
                w = node.rchild
                if t != None:
                    while(t.rchild != None):
                        prev =t
                        t = t.rchild
                    node.value = t.value
                    #del(t)
                    t.set_to_none()
                    #if t.lchild != None:
                     #   if prev.lchild == t:
                      #      prev.lchild = t.lchild
                       # else:
                        #    prev.rchild = t.lchild
                else:
                    if w != None:
                        node.value = w.value
                        node.lchild = w.lchild
                        node.rchild = w.rchild
                        #del(w)
                        w.set_to_none()
                    else:
                        #del(node)
                        node.set_to_none()


    def postorder(self,node):
        if(node.value!=None):
            if node.lchild is not None:
                self.postorder(node.lchild)
            if node.rchild is not None:
                self.postorder(node.rchild)
            print node.value,
    def printtree(self):
        if(self.root.value == None):
            print "None"
        else:
            if self.root.lchild is not None:
                self.postorder(self.root.lchild)
            if self.root.rchild is not None:
                self.postorder(self.root.rchild)
            print self.root.value,



if __name__ == '__main__':
    main()
    n = input("Enter number of values")
    mango = Tree()
    for i in range(n):
        mango.insert(input(),mango.root)
    mango.printtree()
    print ("")
    operations = input("Enter no. of operations")
    for i in range(operations):
        ops=raw_input("Enter operation")
        num=input("Enter no.")
        if ops=='i':
            mango.insert(num,mango.root)
        elif ops=='d':
            mango.remove(num,mango.root)
        else:
            print "invalid operation"
    mango.printtree()
