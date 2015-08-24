__author__ = 'Administrator'
class Stack:
    def __init__(self,size = 16):
        self.stack = []
        self.size = size
        self.top = -1
    def setSize(self, size):
        self.size = size
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def isFull(self):
        if self.top +1 == self.size:
            return True
        else:
            return False
    def top(self):
        if self.isEmpty():
            raise Exception("StackIsEmpty")
        else:
            return self.stack[self.top]
    def push(self,obj):
        if self.isFull():
            raise Exception("StackOverFlow")
        else:
            self.stack.append(obj)
            self.top +=1
    def pop(self):
        if self.isEmpty():
            raise Exception("StackIsEmpty")
        else:
            self.top -= 1
            return self.stack.pop()
    def show(self):
        print(self.stack)
print"---------------the Stack-------------------"
s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.show()
s.pop()
s.show()
s.push(6)
s.show()
class Queue:
    def __init__(self,size = 16):
        self.queue = []
        self.size = size
        self.front = 0
        self.rear = 0
    def isEmpty(self):
        return self.rear == 0
    def isFull(self):
        if (self.front - self.rear +1) == self.size:
            return True
        else:
            return False
    def first(self):
        if self.isEmpty():
            raise Exception("QueueIsEmpty")
        else:
            return self.queue[self.front]
    def last(self):
        if self.isEmpty():
            raise Exception("QueueIsEmpty")
        else:
            return self.queue[self.rear]
    def add(self,obj):
        if self.isFull():
            raise Exception("QueueOverFlow")
        else:
            self.queue.append(obj)
            self.rear += 1
    def delete(self):
        if self.isEmpty():
            raise Exception("QueueIsEmpty")
        else:
            self.rear -=1
            return self.queue.pop(0)
    def show(self):
        print(self.queue)
print"---------------the Stack-------------------"
q = Queue(3)
q.add(1)
q.add(2)
q.show()
q.delete()
q.show()