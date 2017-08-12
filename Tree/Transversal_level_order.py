class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
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

# print nodes at certain level
def print_given_level(tree, l):
  if tree == None:
    return
  if l == 1:
    print(tree.root)
  elif l > 1:
    print_given_level(tree.left, l-1)
    print_given_level(tree.right, l-1)

def print_tree_levelorder(tree):
  if tree == None:
    return
  h = height(tree)
  for i in range(1, h+1):
    print_given_level(tree, i)

# Use queue to level order print a tree
def print_tree_levelorder_q(tree):
  if tree == None:
    return
  # create an empty queue, and put root into the queue to get started
  que = []
  que.append(tree)
  # transverse the tree using the queue, and do the following for each node in the queue:
  # 1. print it
  # 2. deque the node
  # 3. enqueue its left and then right node
  while len(que) > 0:
    node = que.pop(0)
    print(node.root)
    if node.left is not None:
      que.append(node.left)
    if node.right is not None:
      que.append(node.right)
    

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)

# print(height(T))
# print_given_level(T, 3)
print_tree_levelorder_q(T)
