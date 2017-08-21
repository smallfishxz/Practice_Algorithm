class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None
    
def print_linkedlist(l):
  p = l
  while p:
    print(p.data)
    p = p.next
 
def kth_to_last(link_l, k):
  slow = link_l
  fast = link_l
  i = 0
  
  for i in range(k):
    if fast == None:
      return None
    else:
      fast = fast.next
  
  while fast:
    fast = fast.next
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

print(kth_to_last(mylist, 6).data)
