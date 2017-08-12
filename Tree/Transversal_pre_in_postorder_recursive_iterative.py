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

# reference: http://www.geeksforgeeks.org/iterative-preorder-traversal/
def print_tree_inorder_iterative(tree):
  if tree == None: return
  node = tree
  nodestack = []
  # Goes the the leftmost node, push the node along the way into the stack
  while node is not None:
    nodestack.append(node)
    node = node.left
  # transversal the tree. Do the following for each node in the stack:
  # 1. print it
  # 2. if its right node is not null, push it and all notes along to its leftmost node into the stack
  while len(nodestack) > 0:
    node = nodestack.pop()
    print(node.root)
    if node.right is not None:
      node = node.right
      while node is not None:
        nodestack.append(node)
        node = node.left

def print_tree_postorder(tree):
  if tree == None: return
  print_tree_postorder(tree.left)
  print_tree_postorder(tree.right)
  print(tree.root)

# reference: http://www.geeksforgeeks.org/iterative-postorder-traversal/
def print_tree_postorder_iterative(tree):
  # Use 2 stacks. The reserve stack of the final stack to print out is easy to get - some moinor modification on top of preorder iterative. (root - right - left). 
  # As for preorder iterative change, push to stack instead of print, and push left subtree and then right subtree
  # preoder iterative itself needs 1 stack, so a 2nd stack is needed
  if tree == None: return
  node = tree
  nodestack1 = []
  nodestack2 = []
  
  nodestack1.append(node)
  while len(nodestack1) > 0:
    node = nodestack1.pop()
    nodestack2.append(node)
    if node.left is not None:
      nodestack1.append(node.left)
    if node.right is not None:
      nodestack1.append(node.right)
  
  while len(nodestack2) > 0:
    print(nodestack2.pop())

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)

print_tree_preorder_interative(T)
