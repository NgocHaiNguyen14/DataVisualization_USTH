import networkx as nx
import matplotlib.pyplot as plt

# Parameters for the planted partition graph
l = 4  # Number of groups
k = 10  # Number of nodes per group
p_in = 0.7  # Intra-group connection probability
p_out = 0.03  # Inter-group connection probability

# Generate the graph
G = nx.generators.planted_partition_graph(l, k, p_in, p_out)

# Assign a group color for visualization
group_colors = []
for group_id in range(l):
    group_colors.extend([group_id] * k)  # Each group gets `k` nodes

# Generate a layout
pos = nx.spring_layout(G, seed=42)  # Ensure reproducibility

# Color map for groups
color_map = ['red', 'blue', 'green', 'orange']  # Unique color per group

# Map group IDs to colors
node_colors = [color_map[group] for group in group_colors]

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=100, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(
    G, pos, font_size=10, font_color="black"
)

# Add a title and show the graph
plt.title("Planted Partition Graph with 4 Groups", fontsize=16)
plt.show()
