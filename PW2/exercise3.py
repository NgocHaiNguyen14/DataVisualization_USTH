import networkx as nx
import matplotlib.pyplot as plt


def draw_g_with_path(G, pos, start, end):
    """
    Draw the graph with the shortest path between two nodes highlighted.
    """
    # Compute the shortest path
    try:
        shortest_path = nx.shortest_path(G, source=start, target=end, weight='travel_time')
    except nx.NetworkXNoPath:
        print(f"No path exists between {start} and {end}.")
        return

    # Extract edges in the shortest path
    path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
    
    # Draw all nodes and edges
    plt.figure(figsize=(16, 12))
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="gray")
    nx.draw_networkx_nodes(G, pos, node_size=20, node_color="blue")

    # Highlight the shortest path
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_size=50, node_color="red")
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, edge_color="red")
    
    # Add labels for nodes
    nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, "name"), font_size=8, font_color="black")
    
    # Add a title
    plt.title(f"Shortest Path from {start} to {end}")
    plt.show()


def graph_from_metro_file(file_path):
    """
    Reads a file and creates a graph for the metro network.
    """
    # Read file
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = [l for l in file.readlines() if l != '\n']

    begin_nodes = lines.index('noms sommets\n')
    begin_node_attrs = lines.index('coord sommets\n')
    begin_edges = lines.index('arcs values\n')

    nodes = lines[begin_nodes + 1:begin_node_attrs]
    nodes_attrs = lines[begin_node_attrs + 1:begin_edges]
    edges = lines[begin_edges + 1:]

    # Create graph
    G = nx.DiGraph()
    pos = {}
    for node in nodes:
        node, name = node.strip().split(' ', 1)
        node = int(node)
        G.add_node(node, name=name)
        pos[node] = (0, 0)

    for attr in nodes_attrs:
        node, x, y = attr.strip().split()
        node = int(node)
        G.nodes[node]['position'] = (float(x), float(y))
        pos[node] = (float(x), float(y))

    for edge in edges:
        if edge == '\n':
            continue
        node1, node2, travel_time = edge.strip().split()
        node1, node2, travel_time = int(node1), int(node2), float(travel_time)
        G.add_edge(node1, node2, travel_time=travel_time)

    return G, pos


# Load the graph
G, pos = graph_from_metro_file('Ressources/metro')

# Example usage: Visualize the graph with shortest path highlighted
start_node = int(input("The ID of start place: "))
end_node = int(input("The ID of destination: "))
draw_g_with_path(G, pos, start=start_node, end=end_node)
