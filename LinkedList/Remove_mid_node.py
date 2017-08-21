class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
def print_linkedlist(l):
  p = l
  while p:
    print(p.data)
    p = p.next

# remove middle node, but given only the access to this node without the head node 
def delete_mid(mid_n):
  if mid_n == None or mid_n.next == None:
    return False
  # set the middle node's data as the next node's data
  # then remove the next node
  mid_n.data = mid_n.next.data
  mid_n.next = mid_n.next.next
  return True

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

print(delete_mid(n4))
print('-----------')

print_linkedlist(mylist)
