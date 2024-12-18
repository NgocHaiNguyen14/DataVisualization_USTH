import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
G = nx.DiGraph()
G.add_edges_from([
    ('s', 'a', {'weight': 10}),
    ('s', 'c', {'weight': 5}),

    ('a', 'c', {'weight': 2}),
    ('a', 'b', {'weight': 1}),

    ('b', 'd', {'weight': 4}),

    ('c', 'a', {'weight': 3}),
    ('c', 'b', {'weight': 9}),
    ('c', 'd', {'weight': 2}),
    
    ('d', 'b', {'weight': 6}),
    ('d', 's', {'weight': 7}),
    
])
pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
shortest_paths = nx.shortest_path(G, source='s', weight='weight')
print("The shortest paths: ")
print(shortest_paths)
print("exercise 2 is done!")