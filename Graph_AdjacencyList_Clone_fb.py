class Vertex_fb:
  def __init__(self, data):
    self.data = data
    self.neighbours = list()
  
  def add_neighbour_fb(self, v_n):
    if v_n not in self.neighbours:
      self.neighbours.append(v_n)

class Graph_l_fb:
  def __init__(self):
    self.vertices = list()
  
  def add_vertex_fb(self, vertex):
    # data_l=[]
    # for v in self.vertices:
    #   data_l.append(v.data)
    # print("Current data_l: {}".format(data_l))
    # if isinstance(vertex, Vertex_fb) and vertex.data not in data_l:
    if isinstance(vertex, Vertex_fb) and vertex not in self.vertices:
      self.vertices.append(vertex)
      return True
    else:
      return False
  
  def get_vertex(self, n):
    for ii in range(len(self.vertices)):
      # print(ii, self.vertices[ii], self.vertices[ii].data)
      if n == self.vertices[ii].data:
        return self.vertices[ii]
  
  def add_edge_fb(self, vetex_u, vetex_v):
    data_l=[]
    for vetex in self.vertices:
      data_l.append(vetex.data)
    if vetex_u.data in data_l and vetex_v.data in data_l:
      for vertex in self.vertices:
        if vertex.data == vetex_u.data:
          vertex.add_neighbour_fb(vetex_v)
        if vertex.data == vetex_v.data:
          vertex.add_neighbour_fb(vetex_u)
      return True
    else:
      return False
  
  def print_graph_fb(self):
    for vertex in self.vertices:
      l_neighbours_d = []
      for v_neighbour in vertex.neighbours:
        l_neighbours_d.append(v_neighbour.data)
      print("{}:{}".format(vertex.data, l_neighbours_d))
  
  def print_graph_fb2(self):
    for vertex in self.vertices:
      l_neighbours = []
      l_neighbours_d = []
      for v_neighbour in vertex.neighbours:
        l_neighbours.append(v_neighbour)
        l_neighbours_d.append(v_neighbour.data)
      print("{}:{}".format(vertex.data, l_neighbours_d))
      print("{}:{}".format(vertex, l_neighbours))

def clone_l_fb(G1):
  G2 = Graph_l_fb()
  old2new = {}
  for v_old in G1.vertices:
    v_new = Vertex_fb(v_old.data)
    old2new[v_old] = v_new
    # print(v_old.data, v_old)
    # print(v_new.data, v_new)
    G2.vertices.append(v_new)
  print(old2new)
  
  for v_old in G1.vertices:
    for neighbour in v_old.neighbours:
      # print(old2new[v_old])
      # print(neighbour)
      old2new[v_old].add_neighbour_fb(old2new[neighbour])
  return G2
  
g = Graph_l_fb()
for i in range(ord('A'), ord('K')):
  g.add_vertex_fb(Vertex_fb(chr(i)))
# for t in g.vertices:
#   print(t.data, t)
#   print(g.get_vertex(t.data))
g.print_graph_fb2()

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
for edge in edges:
  # print(edge[:1])
  # print(g.get_vertex(edge[:1]))
  # print(edge[1:])
  # print(g.get_vertex(edge[1:]))
  g.add_edge_fb(g.get_vertex(edge[:1]), g.get_vertex(edge[1:]))
g.print_graph_fb()
g.print_graph_fb2()

rpl_g = clone_l_fb(g)
rpl_g.print_graph_fb()
