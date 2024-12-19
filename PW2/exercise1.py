import networkx as nx
import matplotlib.pyplot as plt


def draw_g(G):
	nx.draw_networkx(G)
	plt.show()
	
def graph_from_metro_file(file_path):
  # read file
  with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    lines = [l for l in file.readlines() if l != '\n']

  begin_nodes = lines.index('noms sommets\n')
  begin_node_attrs = lines.index('coord sommets\n')
  begin_edges = lines.index('arcs values\n')

  nodes = lines[begin_nodes + 1:begin_node_attrs]
  nodes_attrs = lines[begin_node_attrs + 1:begin_edges]
  edges = lines[begin_edges + 1:]

  # create graph
  G = nx.DiGraph()
  pos = {}
  for node in nodes:
    node, name = node.strip().split(' ', 1)
    node = int(node)
    G.add_node(node, name=name)
    pos[node] = (0, 0)

  for attr in nodes_attrs:
    node, x, y = attr.strip().split()
    node = int(node)
    G.nodes[node]['position'] = (float(x), float(y))
    pos[node] = (float(x), float(y))

  for edge in edges:
    if edge == '\n':
      continue
    node1, node2, travel_time = edge.strip().split()
    node1, node2, travel_time = int(node1), int(node2), float(travel_time)
    G.add_edge(node1, node2, travel_time=travel_time)

  return G, pos

G, pos = graph_from_metro_file('Ressources/metro')
# print(pos[375])
# draw_g(G)

plt.figure(figsize=(16, 12))
nx.draw_networkx(G, pos=pos, with_labels=True, node_size=20)
plt.show()