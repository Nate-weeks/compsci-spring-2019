"""
 LinkedStack.py - code by Nate Weeks to implement a stack with a linked list
 February 2019

>>> stack = LinkedStack([1,2,3,4])
>>> stack.push(5)
>>> len(stack)
5
>>> stack.pop()
5
>>> stack.isEmpty()
False
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self, values = []):
        self.first = None
        self.last = None
        for value in values:
            self.push(value)
    def __len__(self):
        result = 0
        node = self.first
        while node:
            result += 1
            node = node.next
        return result
    def isEmpty(self):
        return self.first == None
    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    def pop(self):
        top_node = self.last
        node = self.first
        while node:
            if node.next == self.last:
                self.last = node
            node = node.next
        if top_node == self.last:
            self.last = None
            self.first = None
        return top_node.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
