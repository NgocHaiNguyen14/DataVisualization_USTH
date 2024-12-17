import networkx as nx
import matplotlib.pyplot as plt

def mydraw(G, edges_to_color):
    """
    Draw the graph G, coloring specific edges.

    Parameters:
        G (networkx.Graph): The graph to be drawn.
        edges_to_color (list of tuple): The list of edges to color (source, target).

    """
    # Get positions for all nodes
    pos = nx.spring_layout(G)  # Spring layout for aesthetics

    # Draw the entire graph with default settings
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=800)

    # Highlight the specified edges
    nx.draw_networkx_edges(
        G, pos, edgelist=edges_to_color, edge_color="red", width=2.5
    )

    # Display the graph
    plt.title("Graph with Highlighted Edges")
    plt.show()


# Example usage
# Create a graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3), (4, 2)])

# List of edges to color
edges_to_color = [(1, 3), (3, 4)]

# Draw the graph with colored edges
mydraw(G, edges_to_color)
