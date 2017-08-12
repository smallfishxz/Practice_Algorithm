# Tree reference: http://www.openbookproject.net/thinkcs/python/english2e/ch21.html

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

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.root)
    print_tree_inorder(tree.right)

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.root)

def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print('  ' * level + str(tree.root))
    print_tree_indented(tree.left, level+1)

# reference: https://stackoverflow.com/questions/40091369/given-a-binary-tree-print-all-root-to-leaf-paths-using-scipy
def parse(tree, p):
    path = p[:]
    print(path)
    path.append(str(tree.root))
    print(path)
    if tree.left == None and tree.right == None:
        print('-'.join(path))
    else: 
        #Here I assume get_left() returns some falsey value for no left child
        left = tree.left
        if left:
            parse(left, path)
        right = tree.right
        if right:
            parse(right, path)

# To improve memory usage and avoid copy the path, add a pop function so that whenever the recursive call goes up one level 
# to its caller, the corresponding tree node value is popped up from the current path, otherwise, you will get 
# A-B-D, A-B-D-C-E, A-B-D-C-E-F. 
# This problem doesn't eixst when you have a local copy of the path for each recursive call, then the passed input parameter p 
# wont be changed, as in above parse function.
def parse1(tree, path):
#     print(path)
    path.append(str(tree.root))
#     print(path)
    if tree.left == None and tree.right == None:
        print('-'.join(path))
    else:   
        left = tree.left
        if left:
            parse1(left, path)
        right = tree.right
        if right:
            parse1(right, path)
    print(path.pop())

# Iterative print full path: 
# https://www.quora.com/How-do-I-print-all-root-to-leaf-paths-in-binary-tree-iteratively/answer/Siddharth-Teotia?srid=TLNE   
    
sub_tree_r = Tree('C', Tree('E'), Tree('F'))
sub_tree_l = Tree('B', Tree('D'))
T = Tree('A', sub_tree_l, sub_tree_r)

# print_tree_indented(T,0)
parse1(T,[])
