'''
create-graph.py - a program to build a graph for knight's path
Nate Weeks frebruary 2019
'''

def createArray(size):
    '''given a size, creates a size by size 2d array'''
    array = []
    count = 0
    pos = 0
    for x in range(size):
        array.append([])
        for y in range(size):
            array[count].append(pos)
            pos += 1
        count += 1
    return array

def creategraph(array):
    '''given a 2d array, creates a graph of every possible knight's move'''
    graph = {}
    size = len(array)
    knightmoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for x in range(size):
        for y in range(size):
            graph.update({array[x][y]: {}})
            for move in knightmoves:
                new_x = x + move[0]
                new_y = y + move[1]
                if new_x in range(size) and new_y in range(size):
                    graph[array[x][y]].update({array[new_x][new_y]: True})
    return graph

def search(graph, start, which, function):
    """ depth-first or breadth-first  search """
    visited = {}               # Nodes which we're done with.
    if which == 'depth':       # Create a fringe of nodes-to-visit ...
        fringe = Stack()           # ... either a stack
    else:
        fringe = Queue()           # ... or a queue.
    fringe.push(start)         # Initialize the search.
    while len(fringe) > 0:     # Search loop:
        node = fringe.pop()                    # Get node to process.
        visited[node] = True                   # Mark it as 'processed'.
        function(node)                         # Do something with it.
        neighbors = sorted(graph[node].keys()) # Get neighbors.
        for candidate in neighbors:            # Add new ones to fringe.
            if not candidate in visited and not candidate in fringe:
                fringe.push(candidate)

class Stack:
    """ first in, last out
        >>> s = Stack()
        >>> s.push(1); s.push(2); s.push(3)
        >>> 1 in s
        True
        >>> (s.pop(), s.pop(), s.pop())
        (3, 2, 1)
        >>> len(s)
        0
    """
    def __init__(self):
        self.values = []
        self.has = {}    # also put values in a dictionary
    def __len__(self):
        return len(self.values)
    def __contains__(self, value):
        # implement the "_ in _" python syntax.
        return value in self.has
    def push(self, value):
        self.values.append(value)
        self.has[value] = True
    def pop(self):
        value = self.values.pop()
        self.has.pop(value)   # remove from dictionary
        return value

class Queue(Stack):
    """ first in, first out
        >>> q = Queue()
        >>> q.push(1); q.push(2); q.push(3)
        >>> 5 in q
        False
        >>> (q.pop(), q.pop(), q.pop())
        (1, 2, 3)
        >>> len(q)
        0
    """
    def pop(self):
        value = self.values.pop(0)
        self.has.pop(value)
        return value

class Recorder:
    """ A callable object (i.e. acts like a function)
        which can store things and replay them.
          >>> record = Recorder()
          >>> record('a')
          >>> record('b')
          >>> record.replay()
          ' -> a -> b'
    """
    def __init__(self):
        self.memory = ""
        self.length = 0
    def __call__(self, data):
        # (Defines what to do when an instance is treated like a function.)
        self.memory += ' -> ' + str(data)
        self.length += 1
    def replay(self):
        return self.memory

array = createArray(16)
graph = creategraph(array)
record = Recorder()
search(graph, 1, 'depth', record)
print(record.replay())
