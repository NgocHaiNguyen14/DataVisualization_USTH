import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import read_dot

# Step 1: Read the graph from the DOT file
G_dot = read_dot("exercise2.dot")

# Step 2: Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx(
    G_dot, 
    node_color="lightgreen", 
    node_size=800, 
    font_size=12, 
    arrows=True
)
plt.title("Graph from DOT File")
plt.show()

