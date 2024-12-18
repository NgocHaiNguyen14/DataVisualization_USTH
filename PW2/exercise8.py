import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt

# Parameters for the planted partition graph
l = 4  # Number of groups
k = 10  # Number of nodes per group
p_in = 0.7  # Intra-group connection probability
p_out = 0.03  # Inter-group connection probability

# Generate the graph with 40 vertices
G = nx.generators.planted_partition_graph(l, k, p_in, p_out)

# Extract ground truth communities
gt_part = [set(range(k * i, k * (i + 1))) for i in range(l)]

# Detect communities using the Louvain method
partition = community_louvain.best_partition(G)

# Assign colors based on detected communities
colors = [partition[node] for node in G.nodes()]

# Create a color map for visualization
unique_communities = list(set(colors))
color_map = plt.cm.get_cmap('tab20', len(unique_communities))

# Plot the graph with the Louvain-detected communities
plt.figure(figsize=(10, 10))
nx.draw(G, node_color=[color_map(c) for c in colors], with_labels=True, font_weight='bold', node_size=500, font_size=10)
plt.title('Graph with Louvain-detected Communities')
plt.show()

# Function to compare detected communities with ground truth
def compare_communities(gt_part, partition):
    detected_communities = {}
    for node, community in partition.items():
        if community not in detected_communities:
            detected_communities[community] = set()
        detected_communities[community].add(node)

    # Compare the detected communities with the ground truth
    comparison = []
    for i, gt_community in enumerate(gt_part):
        detected_community = detected_communities.get(i, set())
        comparison.append((gt_community, detected_community))

    return comparison

# Compare the ground truth with the detected communities
comparison = compare_communities(gt_part, partition)

# Print the comparison results
for i, (gt_community, detected_community) in enumerate(comparison):
    print(f"Ground truth community {i}: {gt_community}")
    print(f"Detected community {i}: {detected_community}")
    print(f"Intersection: {gt_community & detected_community}")
    print()

