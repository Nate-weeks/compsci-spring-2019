'''
    BinaryTree.py - A basic implementation of a Binary Tree with a recursive
    algorithm to count the height of the tree - Nate Weeks - February 2019
    
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def subtree_length(self):
        if self.value == None:
            return 0
        else:
            count = 0
            if self.right:
                count += 1
                count += self.right.subtree_length()
            if self.left:
                count += 1
                count += self.left.subtree_length()
        return count

class BinaryTree:
    def __init__(self, root):
        self.root = root
    def __len__(self):
        return 1 + self.root.subtree_length()


def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    f.left = g
    f.right = h
    tree = BinaryTree(a)
    print(len(tree))

main()
