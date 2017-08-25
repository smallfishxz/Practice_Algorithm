class Queue:
  def __init__(self):
    self.items = []
    
  def add(self, item):
    self.items.append(item)
  
  def remove(self):
    self.items.pop(0)
  
  def peek(self):
    return self.items[0]
  
  def is_empty(self):
    return self.items == []
  
  def print_queue(self):
    if self.is_empty():
      print('Empty queue!')
    for i in self.items:
      print(i)
  
myqueue = Queue()
myqueue.print_queue()
print('-------------')
myqueue.add(1)
myqueue.add(2)
myqueue.add(3)
myqueue.print_queue()
print('-------------')
print(myqueue.peek())
print('-------------')
myqueue.remove()
myqueue.print_queue()
