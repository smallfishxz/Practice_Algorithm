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
      
#    
def kth_to_last(linked_l, k):
  fast = linked_l.head
  slow = linked_l.head
  
  for i in range(k):
    if fast == None:
      return None
    fast = fast.next
  
  while fast:
    fast = fast.next
    slow = slow.next
  
  return slow.data 
    
    
mylist = linkedlist()

mylist.add(6)
mylist.add(5)
mylist.add(4)
mylist.add(3)
mylist.add(2)
mylist.add(1)

mylist.print_linkedlist()
print('------------')
print(kth_to_last(mylist,3))
