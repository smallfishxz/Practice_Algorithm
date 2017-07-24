# Alternative formulation 

# A slightly different formulation requires to clone a graph given only the Vertex structure and a reference 
# to one "root" vertex. In this version, we should require that all the graph vertices are accessible through a directed path 
# from the given root vertex. 
# On top of the complexity of mapping old vertices to new ones, the candidate is now also required to perform a graph scan. 
# Example of a python implementation to this formulation:

class V:
  def __init__(self, data):
    self.data = data
    self.edges = []

def clone(v1):
  return clone_helper(v1, {})

def clone_helper(v, old2new):
  if v not in old2new:
    # build up the new vertex first
    old2new[v] = V(v.data) 
    # recursively build up the edges for the new vertex
    old2new[v].edges = [clone_helper(e, old2new) for e in v.edges]
  return old2new[v]


