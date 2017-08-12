# reference: http://www.geeksforgeeks.org/print-left-view-binary-tree/
class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

# left view is the first node of each level. So just modify the level order trasversal and enque the left child only
def print_tree_leftview(tree):
  if tree == None:
    return
  # create an empty queue, and put root into the queue to get started
  que = []
  que.append(tree)
  # transverse the tree using the queue, and do the following for each node in the queue:
  # 1. print it
  # 2. deque the node
  # 3. enqueue its left only
  while len(que) > 0:
    node = que.pop(0)
    print(node.root)
    if node.left is not None:
      que.append(node.left)

# Recursive function pritn left view of a binary tree
# Use max_level as global variable.
# Actually didnt quite get to use global  varable, but if not and set max_level as 0 in the util func, all nodes will be printed out..
max_level = 0

def leftViewUtil(tree, level):
    global max_level
    # Base Case
    if tree is None:
        return
 
    # If this is the first node of its level
    if (max_level < level):
        print(tree.root)
        print('level is {}'.format(level))
        print('max_level before is {}'.format(max_level))
        max_level = level
        print('max_level after is {}'.format(max_level))
 
    # Recur for left and right subtree
    leftViewUtil(tree.left, level+1)
    leftViewUtil(tree.right, level+1)
 
# A wrapper over leftViewUtil()
def leftView(tree):
    leftViewUtil(tree, 1)

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)

# print_tree_leftview(T)
leftView(T)
