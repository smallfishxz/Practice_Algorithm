# reference: http://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/
class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.root)

def get_tree_size(tree):
  if tree == None:
    return 0
  else:
    return get_tree_size(tree.left) + get_tree_size(tree.right) + 1

sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)


print(get_tree_size(T))
