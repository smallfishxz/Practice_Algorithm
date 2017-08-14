class tree():
  def __init__(self, root, left = None, right = None):
    self.root = root
    self.left = left
    self.right = right
  
def node_value(node):
  return node.root
# convert tree to its mirror tree
def mirror_tree(tree):
  # base case: tree is empty
  if tree == None:
    return
  # convert left sub-tree and right sub-tree
  left = mirror_tree(tree.left)
  right = mirror_tree(tree.right)
  # swap left sub-tree with right sub-tree
  tree.left = right
  tree.right = left
  
  return tree
  
def print_tree_preorder(tree):
  if tree == None:
    return
  print(tree.root)
  print_tree_preorder(tree.left)
  print_tree_preorder(tree.right)

# Decide whether two trees are mirror to each other
# If they are, it means that the following conditions are all met:
# 1. tree a root value = tree b root value
# 2. tree a left sub-tree is mirror to tree b right sub-tree
# 3. tree a right sub-tree is mirror to tree b left sub-tree
def is_mirror(a, b):
  # base case: a and b are both empty, then they are mirror
  if a == None and b == None:
    return True
  
  # if a == None or b == None:
  #   return False
  
  return a.root == b.root and is_mirror(a.left, b.right) and is_mirror(a.right, b.left)
    
sub_tree_l = tree('B', tree('D'))
sub_tree_r = tree('C', tree('E'), tree('F'))
T = tree('A', sub_tree_l, sub_tree_r)

sub_tree_r = tree('B', None, tree('D'))
sub_tree_l = tree('C', tree('F'), tree('G'))
T1 = tree('A', sub_tree_l, sub_tree_r)

# print_tree_preorder(mirror_tree(T))
print_tree_preorder(T1)
print(is_mirror(T, T1))
