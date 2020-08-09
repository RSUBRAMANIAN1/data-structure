
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)      # recursion
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if(self.left):
            self.left.print()
        print(self.data)
        if(self.right):
            self.right.print()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print()
