# Reference: http://www.geeksforgeeks.org/iterative-preorder-traversal/

class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

def print_tree_preorder(tree):
    if tree == None: return
    print(tree.root)
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)


def print_tree_preorder_interative(tree):
    # base case
    if tree == None:
      return
    # create an empty stack and push root node of the tree into it
    nodestack = []
    nodestack.append(tree)
    # pop all items one by one. Do following for every popped node:
    # 1. print it
    # 2. push its right child
    # 3. push it left child
    # Note that right child is pushed first so that left child is processed first
    while len(nodestack) > 0:
      node = nodestack.pop()
      print(node.root)
      if node.right is not None:
        nodestack.append(node.right)
      if node.left is not None:
        nodestack.append(node.left)

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.root)
    print_tree_inorder(tree.right)


def print_tree_inorder_iterative(tree):
  if tree == None: return
  node = tree
  nodestack = []
  while node is not None:
    nodestack.append(node)
    node = node.left
  
  while len(nodestack) > 0:
    node = nodestack.pop()
    print(node.root)
    if node.right is not None:
      node = node.right
      while node is not None:
        nodestack.append(node)
        node = node.left

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)

print_tree_preorder_interative(T)
