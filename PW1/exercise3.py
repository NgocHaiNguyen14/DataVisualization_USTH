import matplotlib.pyplot as plt
import networkx as nx
# Random graph with 10 nodes and 20 edges
G = nx.gnm_random_graph(10,20)
# Visualization of the graph
nx.draw_networkx(G)
plt.show()
