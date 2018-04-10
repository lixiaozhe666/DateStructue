# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/09 22:12'
class stack:
    def __init__(self):
        self.l=[]
    def instack(self,value):
        self.l.append(value)

    def outstack(self):

        return self.l.pop(-1)

    def printstack(self):
        print (self.l)


class Node:
    def __init__(self,value = None,pNext=None):
        self.value = value
        self.pNext = pNext


class Link:
    def __init__(self):
        self.head = Node(None)
        self.length =0;

    def appendLink(self,value):
        if isinstance(value,Node):
            node = value
        else:
            node =Node(value)
        if self.head.pNext ==None:
            self.head.pNext = node
        else:
            p = self.head
            while p.pNext != None:
                p=p.pNext
            p.pNext = node
        self.length +=1

    def deleteLink(self,value = -1):
        if self.head.pNext ==None:
            print('Lint is null')
            return
        if value ==-1:
            p = self.head
            q = p;
            while p.pNext != None:
                q=p;
                p=p.pNext
            q.pNext =None
        else:
            p = self.head
            q = p;
            while p.value !=value:
                if(p.pNext ==None):
                    print('not value is %s'% value)
                    return
                q = p;
                p = p.pNext
            q.pNext = p.pNext
        self.length -= 1

    def reverseLink(self):#使用栈
        if self.head.pNext ==None:
            return print('link is null')
        p = self.head.pNext
        tempLink = stack()
        i=1
        while i<=self.length:
            tempLink.instack(p.value)
            p = p.pNext
            i +=1
        i=1
        tempLink.printstack()
        p = self.head
        while i<=self.length:
            temp = Node()
            temp.value = tempLink.outstack()
            p.pNext =temp
            p=temp
            i+=1






    def printLink(self):
        p = self.head
        while p.pNext != None:

            p = p.pNext
            print(p.value)



l=Link()
l.appendLink(1)
l.appendLink(2)
l.appendLink(3)
l.appendLink('2222dddd2')
l.printLink()
l.reverseLink()
l.printLink()




