'''
Stack stores the data elements in sequence. 
The data will come out first. 
It can be known Last in First out (LIFO)
Here, we will write some operation to add and remove the element.
'''
class Stack:
    def __init__(self):
        self.stack = list()
    ## a append function to add element
    def push(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False
    ## to look at the top of the stack
    def peek(self):
        return self.stack[-1]
    
    ## to remove element of the stack    
    def pop(self):
        if len(self.stack) < 1:
            return False
        else:
            return self.stack.pop()
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.stack)
s.pop()
print(s.stack)  

'''
The queue concept is same as stack, but queue is first in first out.
'''          
class Queue:
    def __init__(self):
        self.queue = list()
        
    def push(self, item):
        if item not in self.queue:
            self.queue.insert(0, item)
            return True
        else:
            return False
   
    def pop(self):
        if len(self.queue) < 1:
            return False
        else:
            self.queue.pop()
q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.queue)  
q.pop()
print(q.queue)  
          