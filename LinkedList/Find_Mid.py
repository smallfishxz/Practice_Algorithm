class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
def print_linkedlist(l):
  p = l
  while p:
    print(p.data)
    p = p.next

# fast to move at pace of 2 step while slow moves at pace of 1 step
# when fast reaches to the end, slow will be at the middle
def Find_mid(link_l):
  slow = link_l
  fast = link_l
  
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  
  return slow

mylist = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
mylist.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print_linkedlist(mylist)
print('-----------')

print(Find_mid(mylist).data)
