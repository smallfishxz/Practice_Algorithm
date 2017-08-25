# The item in stack records (current item - min(all elements beneath it))
# when item in stack < 0, this item is smaller than the min beneath it, and the stack min at this level will be changed to this item
# when item in stack > 0, this item is bigger than the min beneath it, and the stack min at this level will remain

class MinStack():
  def __init__(self):
    self.stack = []
    self.min = None
  
  # push into the stack (x - min(all below it))
  def push(self, x):
    if not self.stack:
      self.stack.append(x)
      self.min = 0
    else:
      self.stack.append(x - self.min)
      # change the stack min if x is smaller than current min
      if x < self.min:
        self.min = x
  
  # when popping, returns nothing.
  # if popped element negative, means the min value is popped up, so the stack min will be changed after the pop.
  # how to get the new min of the new stack without the popped ele?
  # The current stack min is the actual element in the stack, and what's on top and poped is the different between current element and min(all below the popped), 
  # that is, popped = current/actual element(also self.min) - min(all below the popped), 
  # so min(all below the popped) = self.min - popped 
  # if popped elment is positive, the popped element is not the stack min
  def pop(self):
    x = self.stack.pop()
    if x < 0:
      self.min = self.min - x
  
  # Peek. if x < 0, min is just the actual element; otherwise, current min = min(below elements). 
  # top element in stack = x - min(below elements), so x = top element + min(below elements) = top elements + current min
  def top(self):
    x = self.stack[-1]
    if x > 0:
      return x + self.min
    else:
      return self.min 
  
  def getMin(self):
    return self.min

  def printStack(self):
    size = len(self.stack)
    for i in range(size-1, -1, -1):
      print(self.stack[i])
  
mystack = MinStack()
mystack.push(5)
print(mystack.top())
print('------------')
mystack.push(6)
mystack.push(3)
mystack.push(7)
mystack.push(2)
mystack.printStack()
print('------------')
print(mystack.getMin())
