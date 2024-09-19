class stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size+=1
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            self.stack.remove(self.stack[self.size-1])
            self.size-=1
            return True
        else:
            return False
    
    def peek(self):
        if not self.is_empty():
            return self.stack[self.size-1]
    
s = stack()
s.push(5)
s.push(6)
s.push(4)
print(s.is_empty())
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())