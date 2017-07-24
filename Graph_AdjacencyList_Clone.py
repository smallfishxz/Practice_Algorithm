# Reference: Very good tutorial video on graph representation in python for both adjacency list and adjacency matrx
# Source code are under https://github.com/joeyajames/Python

class Vertex:
  def __init__(self, data):
    self.data = data
    self.neighbours = list()
  
  def add_neighbour(self, n):
    if n not in self.neighbours:
      self.neighbours.append(n)
      self.neighbours.sort()

class Graph_d:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.data not in self.vertices:
      self.vertices[vertex.data] = vertex
      return True
    else:
      return False
  
  def add_edge(self, u, v):
    if u in self.vertices and v in self.vertices:
      for key, value in self.vertices.items():
        if key == u:
          value.add_neighbour(v)
        if key == v:
          value.add_neighbour(u)
      return True
    else:
      return False
      
  def print_graph(self):
    for key in sorted(self.vertices.keys()):
      print("{}:{}".format(key, self.vertices[key].neighbours))
    
class Graph_l:
  def __init__(self):
    self.vertices = list()
  
  def add_vertex(self, vertex):
    data_l=[]
    for v in self.vertices:
      data_l.append(v.data)
    # print("Current data_l: {}".format(data_l))
    if isinstance(vertex, Vertex) and vertex.data not in data_l:
      self.vertices.append(vertex)
      return True
    else:
      return False
  
  def add_edge(self, u, v):
    data_l=[]
    for value in self.vertices:
      data_l.append(value.data)
    if u in data_l and v in data_l:
      for vertex in self.vertices:
        if vertex.data == u:
          vertex.add_neighbour(v)
        if vertex.data == v:
          vertex.add_neighbour(u)
      return True
    else:
      return False
  
  def print_graph(self):
    for vertex in self.vertices:
      print("{}:{}".format(vertex.data, vertex.neighbours))
  
g = Graph_d()
g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
  g.add_vertex(Vertex(chr(i)))
g.print_graph()

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
for edge in edges:
  g.add_edge(edge[:1], edge[1:])
g.print_graph()
