def log(msg=""):
    print(f"-----------------{msg}-----------------------")

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listPrint(self):
        printVal = self.headval
        while printVal is not None:
            print(printVal.dataval,'\n')
            printVal = printVal.nextval
    
    def addNewNodeAtBeggining(self,newData):
        log("Adding New Node at the beginning")
        newNode=Node(newData)
        newNode.nextval=self.headval
        self.headval=newNode

    def addNewNodeAtEnd(self,newData):
        log("Adding New Node at the end")
        newNode=Node(newData)
        if self.headval is None:
            self.headval=newNode
        laste=self.headval
        while (laste.nextval):
            laste=laste.nextval
        laste.nextval=newNode

    def addNewNodeInbetween(self,middle_node,newData):
        log("Adding New Node at the middle")
        if middle_node is None:
            print("The Mentioned Node is not present")
            return
        newNode=Node(newData)
        newNode.nextval=middle_node.nextval
        middle_node.nextval=newNode




        




list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3
print(list1)

list1.addNewNodeAtBeggining("Sun")
list1.addNewNodeAtEnd("Sat")
list1.addNewNodeInbetween(list1.headval.nextval,"Fri")
list1.listPrint()
