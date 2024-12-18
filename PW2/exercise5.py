import networkx as nx
import matplotlib.pyplot as plt

# Parameters for the planted partition graph
l = 4  # Number of groups
k = 10  # Number of nodes per group
p_in = 0.7  # Intra-group connection probability
p_out = 0.03  # Inter-group connection probability

# Generate the graph
G = nx.generators.planted_partition_graph(l, k, p_in, p_out)

# Extract ground truth communities
gt_part = [set(range(k * i, k * (i + 1))) for i in range(l)]
print("Ground Truth Communities:", gt_part)

# Assign colors based on communities
color_map = ['red', 'blue', 'green', 'orange']  # Unique color per group
node_colors = []

# Map nodes to their corresponding community colors
for node in range(len(G.nodes)):
    for community_index, community in enumerate(gt_part):
        if node in community:
            node_colors.append(color_map[community_index])

# Generate a layout
pos = nx.spring_layout(G, seed=42)  # Ensure reproducibility

# Draw the graph with community-based coloring
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=100, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

# Add a title and show the graph
plt.title("Graph with Ground Truth Communities", fontsize=16)
plt.show()
