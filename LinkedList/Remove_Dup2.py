# implement without the class linkedlist

class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
def print_linkedlist(l):
  p = l
  while p:
    print(p.data)
    p = p.next
      
# Use a set to record the transversed nodes   
def remove_dup(linked_l):
  prev = None
  cur = linked_l
  if cur == None:
    return
  s = set()
 
  while cur:
    if cur.data in s:
      prev.next = cur.next
    else:
      s.add(cur.data)
      prev = cur
    cur = cur.next
  
  return linked_l

mylist = Node(77)
n1 = Node(77)
n2 = Node(77)
n3 = Node(31)
n4 = Node(77)
n5 = Node(31)
mylist.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print_linkedlist(mylist)
print('-----------')

print_linkedlist(remove_dup(mylist))
