class node:
  def __init__(self, value = None):
    self.data = value
    self.next = None
    
def printlist(nd):
    p = nd
    while p:
      print(p.data)
      p = p.next

def sumlist(l1, l2):
  # ll is a fakehead. Will retrun ll.next
  ll = node(0)
  # p is used to growing the final linkedlist one node by one node
  p = ll
  carry = 0
  # while any of the list is not None or carry is not 0, the sum wont be end
  while (l1 or l2 or carry != 0):
    # add condition to set individual value as 0 if node is None
    v1 = 0 if l1 == None else l1.data
    v2 = 0 if l2 == None else l2.data
    
    carry, result = divmod((v1 + v2 + carry), 10)
    print(result, carry)
    
    # create a node with value as result, and append it to ll
    r_node = node(result)
    p.next = r_node
    p = r_node
    
    # if l1 or l2 is None, break the loop, this is to avoid refer to Nonetype.next below
    if l1 == None or l2 == None:
      break
    
    # Continue to move to next node in l1 and l2
    l1 = l1.next if l1.next else None
    l2 = l2.next if l2.next else None
  
  return ll.next
    
a = node(8)
n2 = node(6)
a.next = n2
n3 = node(3)
n2.next = n3

b = node(9)
n2 = node(5)
b.next = n2
n3 = node(7)
n2.next = n3

printlist(a)
print('--------')
printlist(b)
print('--------')
print('result,carry')

printlist(sumlist(a, b))
