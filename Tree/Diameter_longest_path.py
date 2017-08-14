class tree():
  def __init__(self, root, left = None, right = None):
    self.root = root
    self.left = left
    self.right = right

def node_value(node):
  return node.root

# reference: http://www.geeksforgeeks.org/diameter-of-a-binary-tree/
def height(tree):
  # base case when tree is empty, then height is 0
  if tree == None:
    return 0
  # tree height is max(left sub-tree height, right sub-tree height) plus 1
  h_l = height(tree.left)
  h_r = height(tree.right)
  return max(h_l, h_r) + 1

# diameter (the longest path between two leaf nodes) could be formed by nodes through the root node or not, thus diameter is generated from the larget of the three:
# 1. if through the root, heigh of left sub-tree + height of right sub-tree + 1
# 2. if not through the root, left sub-tree diameter or right sub-tree diameter
def diameter(tree):
  # Base Case when tree is empty 
  if tree == None:
    return 0
   # Get the height of left and right sub-trees
  h_left = height(tree.left)
  h_right = height(tree.right)
  # Get the diameter of left and irgh sub-trees
  d_left = diameter(tree.left)
  d_right = diameter(tree.right)
  # Return max of the following:
  # 1) Diameter of left subtree
  # 2) Diameter of right subtree
  # 3) Height of left subtree + height of right subtree +1
  return max(d_left, d_right, h_left+h_right+1)

# a more condense way to return diameter and height and  in one recursive function   
def longestPath(n):
  # base case when tree is empty, so that diameter, height as 0, 0
  if n == None:
    return 0, 0
  # get the (diameter, height) of left and right sub-tree
  left_longest, l_height = longestPath(n.left)
  right_longest, r_height = longestPath(n.right)
  # diameter is the larget among left sub-tree diameter, right sub-tree diamater, and left sub-tree height+right sub-tree height+1, while height is max(left sub-tree height, right sub-tree height) + 1
  return max(left_longest, right_longest, l_height+r_height + 1), max(l_height, r_height) + 1
 
sub_tree_l = tree('B', tree('D'))
sub_tree_r = tree('C', tree('E'), tree('F'))
T = tree('A', sub_tree_l, sub_tree_r)

print(longestPath(T))
print(diameter(T))
