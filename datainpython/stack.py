class Stack(object):
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError("超出栈容量")
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("栈空了")
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)
