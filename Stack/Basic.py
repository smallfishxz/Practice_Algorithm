class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
class Stack:
  def __init__(self):
    self.head = None
  
  def push(self, item):
    n = Node(item)
    if self.head == None:
      self.head = n
      return
    n.next = self.head
    self.head = n
  
  def pop(self):
    if self.head == None:
      return None
    tmp = self.head
    self.head = self.head.next
    return tmp.data
    
  def peek(self):
    if self.head == None:
      return None
    return self.head.data
  
  def print_stack(self):
    p = self.head
    while p:
      print(p.data)
      p = p.next
    
mystack = Stack()
mystack.push(3)
mystack.push(4)
print("Current stack is:")
mystack.print_stack()
print("Top element is:")
print(mystack.peek())
v = mystack.pop()
print("After pop the top element, the stack is:")
mystack.print_stack()
print("Popped ele is: {}".format(v))
