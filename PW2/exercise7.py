import networkx as nx
import matplotlib.pyplot as plt

# Parameters for the planted partition graph
l = 4  # Number of groups
k = 10  # Number of nodes per group
p_in = 0.8  # Intra-group connection probability (set to 0.8 as per the exercise)

# Function to calculate modularity
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

# Ground truth communities
gt_part = [set(range(k * i, k * (i + 1))) for i in range(l)]

# Range of p_out values to explore
p_out_values = [i * 0.01 for i in range(0, 101)]  # p_out from 0 to 1 with step 0.01
modularity_values = []

# Loop over different p_out values
for p_out in p_out_values:
    # Generate the graph with the current p_out
    G = nx.generators.planted_partition_graph(l, k, p_in, p_out)
    
    # Calculate the modularity for this graph
    mod = my_modularity(G, gt_part)
    modularity_values.append(mod)

# Plot the modularity curve
plt.plot(p_out_values, modularity_values, label='Modularity')
plt.xlabel('Inter-group connection probability (p_out)')
plt.ylabel('Modularity')
plt.title('Modularity vs p_out for a Planted Partition Graph')
plt.grid(True)
plt.legend()
plt.show()
