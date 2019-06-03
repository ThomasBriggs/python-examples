class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data=[]):
        self.root = None
        if data is not []:
            for i in data:
                self.add(i)

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.addRec(val, self.root)

    def addRec(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.addRec(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.addRec(val, node.right)

    def printNode(self, node):
        if node is not None:
            leftval, rightval = None, None
            if node.left is not None:
                leftval = node.left.val
            if node.right is not None:
                rightval = node.right.val
            s = "Value: {}, Left: {}, Right: {}".format(node.val, leftval, rightval)
            print(s)
        else:
            print("Node is empty")

    def printTree(self):
        if self.root is not None:
            self.printTreeRec(self.root)
        else:
            print("Tree is empty!")

    def printTreeRec(self, node):
        if node is not None:
            self.printNode(node)
            self.printTreeRec(node.left)
            self.printTreeRec(node.right)

    def find(self, id):
        if self.root is not None:
            return self.findRec(id, self.root)
        else:
            print("Tree is empty!")

    def findRec(self, id, node):
        if node is not None:
            if node.val == id:
                return True
            elif node.val < id:
                self.findRec(id, node.right)
            else:
                self.findRec(id, node.left)
        else:
            print("Node not found!")

