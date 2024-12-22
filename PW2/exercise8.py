#venv-data
import partition_networkx
import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.community as nx_comm
from networkx.algorithms.community.quality import modularity
import numpy as np
import community as community_louvain

## Community detection

colors = ['red', 'blue', 'green', 'orange']
l = 4 # number of groups
k = 10 # number of nodes per group
p_in = 0.7 # intra-group probability of connection
p_out = 0.03 # between-group probability of connection
G = nx.generators.planted_partition_graph(l, k, p_in, p_out)
nx.draw_networkx(G)
plt.show()

gt_part = [set(range(k * i, k * (i + 1))) for i in range(l)]
pos = nx.spring_layout(G, seed=42)

for i, part in enumerate(gt_part):
    nx.draw_networkx_nodes(G, pos, nodelist=list(part), node_color=colors[i], label=f"Community {i+1}")

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.show()

def my_modularity(G, communities, k):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    Q = 0.0
    if m == 0:
        return 0
    for i in range(n): 
        for j in range(n):
            ci = i // k
            cj = j // k
            e = 1 if G.has_edge(i, j) else 0
            a_i = 1 if i in communities[ci] else 0
            ki = G.degree(i)
            kj = G.degree(j)
            Q += (a_i - (ki * kj) / (2*m))
    return Q / (2 * m)

# Calculate modularity using my_modularity
my_mod = my_modularity(G, gt_part, k)
print(f"My Modularity: {my_mod}")


p_out_values = np.linspace(0.01, 0.1, 10)
modularity_values = []

for p_out in p_out_values:
    G_temp = nx.planted_partition_graph(l, k, 0.8, p_out)
    gt_part_temp = [set(range(k * i, k * (i + 1))) for i in range(l)]
    modularity_values.append(modularity(G_temp, gt_part_temp))

plt.plot(p_out_values, modularity_values, marker='o')
plt.xlabel("Inter-group Probability (p_out)")
plt.ylabel("Modularity")
plt.title("Modularity vs p_out")
plt.show()


def detect_communities_louvain(G):
    partition = community_louvain.best_partition(G)
    return partition

partition = detect_communities_louvain(G)
print(partition)

colors = [partition[node] for node in G.nodes()]
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.jet)
plt.title("Louvain Method - Community Detection")
plt.show()

mod_louvain = []
mod_gt = []

for p_out in p_out_values:
    G_temp = nx.planted_partition_graph(l, k, 0.8, p_out)
    gt_part_temp = [set(range(k * i, k * (i + 1))) for i in range(l)]

    # Louvain modularity
    partition = community_louvain.best_partition(G_temp)
    louvain_communities = [set([node for node in partition if partition[node] == c]) for c in set(partition.values())]
    mod_louvain.append(modularity(G_temp, louvain_communities))
    
    mod_gt.append(modularity(G_temp, gt_part_temp))

plt.plot(p_out_values, mod_gt, label="Ground Truth", marker='o')
plt.plot(p_out_values, mod_louvain, label="Louvain", marker='x')
plt.xlabel("Inter-group Probability (p_out)")
plt.ylabel("Modularity")
plt.title("Comparison of Modularity")
plt.legend()
plt.show()