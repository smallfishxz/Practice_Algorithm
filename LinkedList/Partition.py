class Node:
  def __init__(self, value = None):
    self.data = value
    self.next = None
    
def printlist(nd):
    p = nd
    while p:
      print(p.data)
      p = p.next

def partition(node, key):
  smaller = None
  smaller_tail = None
  bigger = None
  bigger_tail = None
  
  while node:
    # Isolate the current node by doing the following:
    # 1. Use next to remember current's next node
    # 2. Set the current node's next as None
    next = node.next
    node.next = None
    # if current node's data is smaller than key, append it to the end of the smaller list
    if node.data < key:
      # print('smaller node.data is {}'.format(node.data))
      if smaller == None:
        smaller = node
        smaller_tail = smaller
      else:
        smaller_tail.next = node
        smaller_tail = node
    # Otherwise, append the current node to the bigger list
    else:
      print('bigger node.data is {}'.format(node.data))
      if bigger == None:
        bigger = node
        bigger_tail = bigger
        # print('insert bigger list data is {}'.format(bigger_tail.data))
      else:
        bigger_tail.next = node
        bigger_tail = node
    # move to next node
    node = next
  
  # !!! if the smaller part is None, then directly return the bigger list
  if smaller == None:
    return bigger
  
  # merge the smaller and bigger by appending bigger to smaller  
  smaller_tail.next = bigger
  return smaller
        
    
mylist = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(5)
n5 = Node(10)
n6 = Node(2)
n7 = Node(1)
mylist.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


printlist(mylist)
print('--------')

printlist(partition(mylist, 5))
