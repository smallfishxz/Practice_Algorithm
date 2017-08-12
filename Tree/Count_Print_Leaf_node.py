class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

def get_leaf_count(tree):
  if tree == None:
    return 0
  if tree.left == None and tree.right == None:
    return 1
  else:
    return get_leaf_count(tree.left) + get_leaf_count(tree.right)

def print_leaf_node(tree):
  if tree == None:
    return
  if tree.left == None and tree.right == None:
    print(tree.root)
  else:
    print_leaf_node(tree.left)
    print_leaf_node(tree.right)

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)


print(get_leaf_count(T))
print_leaf_node(T)
