class Queue:

    def __init__(self):
        self.Queue = []
        self.size =0

    def enqueue(self, element):
        self.Queue.append(element)
        self.size+=1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def dequeue(self):
        if not self.is_empty():
            self.size-=1
            return self.Queue.pop(0)
        else:
            return False
        
    def peek(self):
        if not self.is_empty():
            return self.Queue[0]
'''''
queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(4)
print(queue.is_empty())
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
'''