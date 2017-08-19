class Node:
  def __init__(self, value=None):
    self.data = value
    self.next = None

def print_linkedlist(nd):
  p = nd
  while p:
    print(p.data)
    p = p.next
    
def get_size_tail(l):
  p = l
  size = 0
  while p.next:
    size += 1
    p = p.next
  return (p, size)

def get_kth(l, k):
  p = l
  while k > 0 and p:
    p = p.next
    k -= 1
  return p

def is_intersect(l1, l2):
  if l1 == None or l2 == None:
    return None
  
  # Step 1: Transverse 2 lists separately to find tail node and length
  p1, count1 = get_size_tail(l1)
  p2, count2 = get_size_tail(l2)
  
  # Step 2: decide whether intersect - tail node is the same or not
  if p1 != p2:
    return None
  
  # step 3: transverse 2 list simultaneously with longer one chopped out to have the same length
  shorter = l1 if count1 < count2 else l2
  longer = l2 if count1 < count2 else l1
  
  # chopped out the longer list by fast-forward it by the length differences
  longer = get_kth(longer, abs(count1-count2))
  
  while shorter != longer:
    shorter = shorter.next
    longer = longer.next
  
  return shorter
  
mylist1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
mylist1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print_linkedlist(mylist1)
print('----------------')


mylist2 = Node(8)
n7 = Node(7)
n8 = Node(2)
mylist2.next = n7
n7.next = n8
n8.next = n3
print_linkedlist(mylist2)
print('----------------')

print(is_intersect(mylist1, mylist2).data)


