class Node:
  def __init__(self, value=None):
    self.data = value
    self.next = None

def print_linkedlist(nd):
  p = nd
  while p:
    print(p.data)
    p = p.next
    
def is_loop(l):
  slow = l
  fast = l
  
  # when fast meets slow, it proves that there is a loop
  # suppose k steps before entering the loop
  # fast and slow meets at k step behind start of the loop. 
  # Reasons:
  # 1. slow is at the loop start after k steps
  # 2. fast is k steps faster than slow, thus k steps into the loop
  # 3. slow is k steps behind fast, in the other way around, fast is loopsize - k steps behind slow
  # 4. fast catches up slow at pace of 1 step each unit time, so it will take loopsize - k steps for fast to meet slow.
  # 5. When they meet, slow is at loopsize - k steps before loop start, which is k step behind loop start
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      break
  
  if fast == None or fast.next == None:
    return None
  
  # After meeting, move slow to head, which is k step away from loop start
  # Fast is kept as where it is, which is also k step away from loop start
  slow = l
  
  # move forward both simultaneously. When then meet again, it will be at the loop start
  while slow != fast:
    slow = slow.next
    fast = fast.next
  
  # return either
  return slow
  
mylist = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
mylist.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n4
# print_linkedlist(mylist)
print('----------------')


print(is_loop(mylist).data)
