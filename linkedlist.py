class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def createnode(self,no):
        if(self.head == None):
            val = input()
            self.head = Node(val)
        else:
            for i in range(no-1):
                val = input()
                self.next = Node(val)
                self = self.next

    def printnode(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    n = int(input())
    llist.createnode(n)
    llist.printnode()
