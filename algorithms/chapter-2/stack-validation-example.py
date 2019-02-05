'''
stack-validation-example.py - a program by Nate Weeks to check for
properly closing parenthesis - February 2019

>>> parChecker('{{([][])}()}')
True
>>> parChecker('[{()]')
False
>>> parChecker('[({})]}')
False
>>> parChecker('[(]')
False
>>> parChecker('[(])')
False
'''

from LinkedStack import LinkedStack

def parChecker(symbolString):
    s = LinkedStack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
