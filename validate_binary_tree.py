import sys

class Node():
  def __init__(self, value, left = None, right = None):
    self.root = value
    self.left = left
    self.right = right
    
# The intuitive idea is to see whether root node is bigger than the max value of its left subtree max_value(tree.root
# and root node is smaller than the min value of its right subtree, min_value(tree.root), but calling the extra
# function to get max and min value of subtrees means visiting nodes twice. And we could get the min and max value
# along the one-time transversal of the tree, by using a util function to pass along the min and max value

# Time: O(N), Space: O(1)
def valid_B_tree(tree):
  return valid_B_tree_util(tree, -sys.maxsize, sys.maxsize)


def valid_B_tree_util(tree, min_v, max_v):
  if tree == None:
    return True
  
  if tree.root <= min_v or tree.root >= max_v:
    return False
  
  return valid_B_tree_util(tree.left, min_v, tree.root) and \
    valid_B_tree_util(tree.right, tree.root, max_v)
  
# in-order transverse the tree, and get an arary. If the array is sorted ascending, then it is valid binary tree.
# Optimized to not use extra array, so that while transversing compare with its prev node value to see whether
# bigger than prev
# This is somehow not working when writing in python. The prev for node is somehow not right...
# this is working solution under:
# https://github.com/kamyu104/LeetCode/blob/master/Python/validate-binary-search-tree.py

def valid_inorder(tree):
  return valid_inorder_util(tree, -sys.maxsize)
  
def valid_inorder_util(tree, prev):
  if tree == None:
    return True

  left_valid = valid_inorder_util(tree.left, prev)
  
  print(left_valid, tree.root, prev)
  if left_valid == False or tree.root < prev:
    print(left_valid, tree.root, prev)
    return False
 
  
  prev= tree.root
  print(prev)
  return valid_inorder_util(tree.right, prev)
  
# Same error as above...
def valid_inorder2(tree):
  prev = None
  
  if tree: 
    if valid_inorder2(tree.left) == False:
      return False
    if prev is not None and prev.root > tree.root:
      return False
    return valid_inorder2(tree.right)
  
  return True

# bool isValidBSTHelper(Tree *root, int& lastVal) {
#   if (!root) {
#     return true;
#   }

#   bool leftValid = isValidBSTHelper(root->left, lastVal);
#   if (!leftValid || root->val < lastVal) {
#       return false;
#   }

#   lastVal = root->val;
#   return isValidBSTHelper(root->right, lastVal);
# } 

# bool isValidBST(Tree *root) {
#   int minVal = INT_MIN;
#   return isValidBSTHelper(root, minVal);
# }

def inorder(tree):
  if tree == None:
    return
  inorder(tree.left)
  print(tree.root)
  inorder(tree.right)

mytree = Node(3)
node1 = Node(2)
node2 = Node(5)
mytree.left = node1
mytree.right = node2
node3 = Node(1)
node4=Node(4)
mytree.left.left = node3
mytree.left.right = node4

# print(valid_B_tree(mytree))
inorder(mytree)
print('--------------------')
print(valid_inorder(mytree))
