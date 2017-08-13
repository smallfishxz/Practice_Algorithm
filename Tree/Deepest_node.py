class tree():
  def __init__(self, root, left = None, right = None):
    self.root = root
    self.left = left
    self.right = right
  
def node_value(node):
  return node.root
    
  
class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

# Solution 1: Use to functions to find the height of the tree, and print the nodes in the deepest level.
# reference in the level order transversal file
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

# Solution 2
# reference: http://blog.gainlo.co/index.php/2016/04/26/deepest-node-in-a-tree/
# modificatoin on the iterative level order transversal. The deepest node is the last one in the iterative level order transversal queue.
# Use a variable deepest_node to record the first one in the queue. it gets overwritten when each of item in the queue are dequeued, and thus record the last one in the queue to be dequeued.
def find_deepest(tree):
  if tree == None:
    return
  que = []
  que.append(tree)
  # Transvese the tree. While the queue is not empty, do the following for each item dequeued from the queue:
  # 1. recorde the dequeued item in deepest_node
  # 2. dequeue it
  # 3. enqueue its left and right child as long as they are not empty
  while len(que) > 0:
    deepest_node = que[0]
    print(deepest_node.root)
    node = que.pop(0)
    if node.left is not None:
      que.append(node.left)
    if node.right is not None:
      que.append(node.right)
    print('-'.join(map(node_value,que)))
  return deepest_node.root
  

# Solution 3: recursive way
# reference: http://blog.gainlo.co/index.php/2016/04/26/deepest-node-in-a-tree/

def find_deepest2(tree, level):
  if tree == None:
    return (None, 0)
  if tree.left == None and tree.right == None:
    return (tree.root, level)
  deepst_node_l, depth_l = find_deepest2(tree.left, level+1)
  deepst_node_r, depth_r = find_deepest2(tree.right, level+1)
    
  if depth_l > depth_r:
    return (deepst_node_l, depth_l)
  else:
    return (deepst_node_r, depth_r)

sub_tree_l = tree('B', tree('D'))
sub_tree_r = tree('C', tree('E'), tree('F'))
T = tree('A', sub_tree_l, sub_tree_r)

h = height(T)
# print_given_level(T, h)
# print(find_deepest(T))
print(find_deepest2(T, 1))
