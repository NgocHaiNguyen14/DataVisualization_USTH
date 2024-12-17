import networkx as nx
import matplotlib.pyplot as plt

def divGraph(n):
    """
    Generate the graph of divisors for integers between 2 and n.
    Nodes are integers from 2 to n, and there is an edge from i to j
    if i is a multiple of j.
    """
    G = nx.DiGraph()  # Create a directed graph

    # Add nodes and edges
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:  # If i is a multiple of j
                G.add_edge(i, j)
    
    return G

# Example usage
n = 10
G = divGraph(n)

# Visualization of the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx(
    G, 
    with_labels=True, 
    node_color="skyblue", 
    node_size=800, 
    font_size=12, 
    arrows=True
)
plt.title(f"Divisor Graph for Integers from 2 to {n}")
plt.show()
