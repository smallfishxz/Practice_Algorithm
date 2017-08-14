class tree():
  def __init__(self, root, left = None, right = None):
    self.root = root
    self.left = left
    self.right = right

# in-order iterator  
class iterator():
  def __init__(self, tree):
    self.stack = []
    self.left_recur(tree)
  
  def left_recur(self, tree):
    if tree == None:
      return
    self.stack.append(tree)
    self.left_recur(tree.left)

  def next(self):
    if len(self.stack) == 0:
      return None
    next_item = self.stack.pop()
    self.left_recur(next_item.right)
    return next_item  

# in-order iterator transformed from the in-order iterative funvction
class iterator3():
  def __init__(self,tree):
    self.stack = []
    node = tree
    while node is not None:
      self.stack.append(node)
      node = node.left
  
  def next(self):
    if len(self.stack) == 0:
      return None
    next_item = self.stack.pop()
    node = next_item.right
    while node is not None:
      self.stack.append(node)
      node = node.left
    return next_item

# preorder iterator  
class iterator2():
  def __init__(self, tree):
    self.stack = []
    self.stack.append(tree)
  
  def next(self):
    if len(self.stack) == 0:
      return None
    next_item = self.stack.pop()
    if next_item.right is not None:
      self.stack.append(next_item.right)
    if next_item.left is not None:
      self.stack.append(next_item.left)
    return next_item

def node_value(node):
  return node.root

sub_tree_l = tree('B', tree('D'))
sub_tree_r = tree('C', tree('E'), tree('F'))
T = tree('A', sub_tree_l, sub_tree_r)

my_iterator = iterator3(T)
# while (my_iterator.next()):
#   print(my_iterator.next().root)
while True:
  my_node = my_iterator.next()
  if my_node == None:
    break
  print(my_node.root, end="\n")
