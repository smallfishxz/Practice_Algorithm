# Preorder transverse tree

class Tree():
  def __init__(self, value, left = None, right = None):
    self.root = value
    self.left = left
    self.right = right


def preorder(tree):
  if tree == None:
    return
  print(tree.root)
  preorder(tree.left)
  preorder(tree.right)

def store(tree, list):
  if tree == None:
    list.append(None)
  else:
    list.append(tree.root)
    store(tree.left, list)
    store(tree.right, list)
  return list



mytree = Tree(4)
mytree.left = Tree(1)
mytree.right=Tree(5)
mytree.left.left = Tree(3)
mytree.left.right = Tree(2)

preorder(mytree)
print('-------------')

print(store(mytree, []))
