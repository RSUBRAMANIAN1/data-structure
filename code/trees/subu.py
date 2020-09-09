class Node:

    def __init__(self, data): # _init_ -> __init__
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):   # _init_ -> __init__
        self.head = None

    def insertafternode(self, val):
        temp = self.head
        while(temp.data != val):
            temp = temp.next
        ne=input()    
        tmp1 = Node(ne)
        tmp1.next = temp.next
        temp.next = tmp1

    def createnode(self, no):
        if(self.head == None):
            val = input()
            self.head = Node(val)
            if(no > 1):
                for i in range(no-1):
                    val = input()
                    self.next = Node(val)
                    self = self.next

    def printnode(self):
        temp = self.head
        while(temp):
            print(temp.data) #println->print
            temp = temp.next



if __name__ == "__main__":
    llist = LinkedList()

    n = int(input())
    llist.createnode(n)
    #
    llist.insertafternode("hey")
    llist.printnode()