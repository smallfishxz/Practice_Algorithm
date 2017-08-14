class tree():
  def __init__(self, root, left = None, right = None):
    self.root = root
    self.left = left
    self.right = right
  
def node_value(node):
  return node.root

# recursive function to get height of tree. Reference: http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
# base case is Tree as None to have height as 0
def height(tree):
  if tree == None:
    return 0
  hl = height(tree.left)
  hr = height(tree.right)
  # use the larger one
  if hl > hr:
    return hl+1
  else:
    return hr+1

# iterative function to get the height of the tree. 
# reference: http://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/
# Modification on top of the iterative level order transversal to add the outer loop to judge whether reaching the deepest level yet and increase the height number
def height1(tree):
  if tree == None:
    return 0
  # initialize node queue as empty and height as 0
  que = []
  h = 0
  # start from tree root to push it to node queue
  que.append(tree)
  # Loop through and transverse level by level
  while(True):
    # node count to track the count of nodes at current level
    node_count = len(que)
    # If no node at current level, already hit the deepest level, so return height
    if node_count == 0:
      return h
    # If there is still node at current level, increase the height by 1
    else:
      h += 1
    # for all nodes at current level, do the following things:
    # 1. dequeue it 
    # 2. enqueue its left/right child if they are not none
    while(node_count > 0):
      node = que.pop(0)
      if node.left is not None:
        que.append(node.left)
      if node.right is not None:
        que.append(node.right)
      node_count -= 1
    print('-'.join(map(node_value,que)))

# more intuitive modification on top of the iterative tree height function
def height2(tree):
  if tree == None:
    return 0
  # initialize node queue as empty and height as 0
  que = []
  h = 0
  # start from tree root to push it to node queue
  que.append(tree)
  
  # Just a very small change to the iterative tree height function, that is, to have a variable to record the count of nodes in the current level, so that we could maintain a queue to always include nodes at the same level
  while len(que) > 0:
    print('-'.join(map(node_value, que)))
    node_count = len(que) # minor change to height function
    for i in range(node_count): # minor change to height function
      node = que.pop(0)
      if node.left is not None:
        que.append(node.left)
      if node.right is not None:
        que.append(node.right)
    h += 1
  return h
    
sub_tree_l = tree('B', tree('D'))
sub_tree_r = tree('C', tree('E'), tree('F'))
T = tree('A', sub_tree_l, sub_tree_r)

hei = height1(T)
print(hei)
