class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
class linkedlist:
  def __init__(self):
    self.head = None
    
  def add(self, value):
    n = Node(value)
    n.next = self.head
    self.head = n
  
  def print_linkedlist(self):
    p = self.head
    while p:
      print(p.data)
      p = p.next
      
# Use a set to record the transversed nodes   
def remove_dup(linked_l):
  if linked_l == None:
    return
  s = set()
  s.add(linked_l.head.data)
  prev = linked_l.head
  cur = linked_l.head.next
  while cur:
    if cur.data in s:
      prev.next = cur.next
    else:
      s.add(cur.data)
      prev = cur
    cur = cur.next

# use 2 pointers. Cur to loop throu one by one, while runner loops all subsequent nodes for duplicates
def remove_dup1(linked_l):
  if linked_l == None:
    return
  cur = linked_l.head
  while cur:
    runner = cur
    while runner.next:
      if runner.next.data == cur.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    cur = cur.next
    
    
mylist = linkedlist()

mylist.add(31)
mylist.add(77)
mylist.add(31)
mylist.add(77)
mylist.add(77)
mylist.add(77)

mylist.print_linkedlist()
print('------------')
# remove_dup1(mylist)
# mylist.print_linkedlist()
