class Node:
  def __init__(self, value = None):
    self.data = value
    self.next = None
    
def printlist(nd):
    p = nd
    while p:
      print(p.data)
      p = p.next

def is_panlindrome(node):
  slow = node
  fast = node
  nodestack = []
  
  # use slow and fast nodes to push the first half of the list into stack
  while fast and fast.next:
    nodestack.append(slow.data)
    fast = fast.next.next
    slow = slow.next
    # print('slow.data is {}'.format(slow.data))
  
  # Now if len of list is even number, slow is at the start of the second half list, and fast is None
  # but if len of list is odd number, slow is at the middle element of the list, and fast.next is None, we will need to have slow skip this middle element, so that slow could be at the start of the second half
  if fast != None:
    slow = slow.next
  
  while slow:
    print('slow.data is {}'.format(slow.data))
    print('top of node is {}'.format(nodestack[-1]))
    # comparing 
    if slow.data != nodestack.pop():
      return False
    slow = slow.next
  return True
  
mylist = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(9)
# n5 = Node(9)
n6 = Node(8)
n7 = Node(5)
n8 = Node(3)
mylist.next = n2
n2.next = n3
n3.next = n4

# n4.next = n5
# n5.next = n6

n4.next = n6

n6.next = n7
n7.next = n8

printlist(mylist)
print('--------')

print(is_panlindrome(mylist))
