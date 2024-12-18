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

def my_modularity(Graphc, gt_part):
    m = Graphc.number_of_edges()
    modularity = 0.0

    for community in gt_part:

        for i in community:
            for j in community:
                  ki = Graphc.degree(i)
                  kj = Graphc.degree(j)
                  A_ij = 1 if Graphc.has_edge(i, j) else 0
                  modularity += A_ij - (ki * kj) / (2 * m)

    modularity /= (2 * m)
    return modularity

print(my_modularity(G, gt_part))
networkx_modularity = nx.algorithms.community.modularity(G, gt_part)
print("Networkx Modularity:", networkx_modularity)
