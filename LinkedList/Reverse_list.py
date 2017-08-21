class Node:
  def __init__(self, value = None):
    self.data = value
    self.next = None
    
def printlist(nd):
    p = nd
    while p:
      print(p.data)
      p = p.next

def reverse_l(node):
  head = None
  
  # isolate node by node and insert it into the new list
  # how to isolidate:
  # 1. use nxt to remember node.next
  # 2. set node.next as None
  while node:
    nxt = node.next
    node.next = None
    
    # Then insert each node into the head list
    node.next = head
    head = node
    
    # move to next node
    node = nxt
  
  return head

def reverse_and_clone(l):
  head = None
  
  while l:
    n = Node(l.data)
    
    # insert it into head list
    n.next = head
    head = n
    
    # move to next
    l = l.next
    
  return head
  
mylist = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(9)
mylist.next = n2
n2.next = n3
n3.next = n4


printlist(mylist)
print('--------')

# printlist(reverse_l(mylist))

printlist(reverse_and_clone(mylist))
