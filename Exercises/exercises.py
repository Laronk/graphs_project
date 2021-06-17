import json
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
from networkx.drawing.nx_agraph import graphviz_layout

nx.graphviz_layout = graphviz_layout

# read the adjacency list representation
# read .json data to a python list
with open(
    "Jan_Karpiuk.json",
) as data_file:
    data = data_file.read()

adj_list = json.loads(data)
adj_dict = {idx: adj_list[idx] for idx in range(len(adj_list))}

# create graph from dict of lists
G = nx.from_dict_of_lists(adj_dict)

# draw the graph
plt.figure(figsize=(5, 5))
nx.draw_networkx(G, pos=nx.graphviz_layout(G, prog="circo"))
plt.draw()
plt.axis("off")
plt.savefig("Exercises/graph.png")
plt.close()
