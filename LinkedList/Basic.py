class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class linkedlist():
  def __init__(self):
    self.head = None
  
  def isEmpty(self):
    return self.head == None
  
  def add(self, value):
    n = Node(value)
    n.next = self.head
    self.head = n
  
  def size(self):
    count = 0
    p = self.head
    while p:
      count += 1
      p = p.next
    return count
  
  def search(self,item):
    current = self.head
    while current:
      if current.data == item:
        return True
      current = current.next
    return False
  
  #Given a ‘key’, delete the first occurrence of this key in linked list.
  def remove(self,item):
    current = self.head
    if current == None:
      return
    elif current.data == item:
      self.head = current.next
      
    while current.next:
      if current.next.data == item:
        current.next = current.next.next
      current = current.next
  
  def append(self, item):
    end = Node(item)
    current = self.head
    if current == None:
      self.head = end
      return
    while current.next:
      current = current.next
    current.next = end
 
  def print_linkedlist(self):
    p = self.head
    while p:
      print(p.data)
      p = p.next

mylist = linkedlist()

# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

mylist.print_linkedlist()
print(mylist.size())
print(mylist.search(31))
mylist.remove(17)
mylist.print_linkedlist()
mylist.append(17)
mylist.print_linkedlist()
