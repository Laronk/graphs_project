import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from networkx.drawing.nx_agraph import graphviz_layout
import unittest
from algorithm.dijkstra import DijkstraSolver
import json


class MyDijkstraImplementationTestCase(unittest.TestCase):
    def setUp(self):
        self.graphs = []
        self.weight_range = (1, 9)
        self.test_images_folder = "./test_images"
        self.test_dataset_path = "./test_dataset.json"
        nx.graphviz_layout = graphviz_layout
        self.load_testdataset()

    def load_testdataset(self):
        with open(
            "{dataset_path}".format(dataset_path=self.test_dataset_path),
        ) as data_file:
            data = data_file.read()

        test_dataset = json.loads(data)
        incidence_matrixes = [np.array(im) for im in test_dataset]
        adjacency_matrixes = []
        # convert incidence_matrixes to adjacency_matrixes
        for im in incidence_matrixes:
            am = (np.dot(im, im.T) > 0).astype(int)
            np.fill_diagonal(am, 0)  # remove self loops
            adjacency_matrixes.append(am)
        # assign random weights to undirected graphs
        for am in adjacency_matrixes:
            curr_graph = nx.from_numpy_matrix(am)
            for (u, v, w) in curr_graph.edges(data=True):
                w["weight"] = random.randint(self.weight_range[0], self.weight_range[1])
            # create new test graph for each adjacency_matrix
            self.graphs.append(curr_graph)

    def draw_graph_with_path(
        self,
        graph,
        path,
        output_file_name,
        size=7,
        bgcolor="white",
        path_color="red",
        path_width=3,
        prog="circo",
    ):
        # draw randomly generated graph for the current test case
        plt.figure(figsize=(size, size))
        ax = plt.axes()
        ax.set_facecolor(bgcolor)
        pos = nx.graphviz_layout(graph, prog)

        edge_to_color = {edge: "black" for edge in graph.edges()}
        edge_to_width = {edge: 1 for edge in graph.edges()}
        for edge in zip(path, path[1:]):
            if edge in edge_to_color.keys():
                edge_to_color[edge] = path_color
                edge_to_width[edge] = path_width

        params = {
            "edge_color": list(edge_to_color.values()),
            "width": list(edge_to_width.values()),
        }

        nx.draw_networkx(graph, pos, **params)
        plt.draw()
        labels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.savefig(
            "{path}/{file_name}.png".format(
                path=self.test_images_folder, file_name=output_file_name
            )
        )
        plt.close()

    def test_dijkstra_path_length(self):
        for test_nr in range(len(self.graphs)):
            # set currently tested Graph
            G = self.graphs[test_nr]
            test_G = DijkstraSolver(G.copy())
            # set entry and exit nodes for currently tested Graph
            entry_node = 0
            exit_node = random.randint(1, len(G.nodes) - 1)
            with self.subTest(i=test_nr):
                # get the correct path length for dijkstra's algorithm
                correct_path_length = nx.dijkstra_path_length(
                    G, source=entry_node, target=exit_node
                )
                correct_path = nx.dijkstra_path(G, source=entry_node, target=exit_node)
                # get the dijkstra's path length using my implementation of the algorithm
                test_path = test_G.get_min_path(src=entry_node, dest=exit_node)
                # draw currently tested graph
                self.draw_graph_with_path(
                    G,
                    correct_path,
                    output_file_name="{fun_name}_{test_number}".format(
                        fun_name="test_dijkstra_path_length", test_number=test_nr
                    ),
                    size=8,
                    bgcolor="white",
                    prog="circo",
                )
                # compare correct and test path lengths
                self.assertEqual(
                    correct_path_length,
                    test_path["length"],
                    "Incorrect dijkstra path length",
                )

    def test_dijkstra_path(self):
        for test_nr in range(len(self.graphs)):
            G = self.graphs[test_nr]
            test_G = DijkstraSolver(G.copy())
            entry_node = 0
            exit_node = random.randint(1, len(G.nodes) - 1)
            with self.subTest(i=test_nr):
                # get the correct path length for dijkstra's algorithm
                correct_path = nx.dijkstra_path(G, source=entry_node, target=exit_node)
                # get the dijkstra's path length using my implementation of the algorithm
                test_path = test_G.get_min_path(src=entry_node, dest=exit_node)
                # draw currently tested graph
                self.draw_graph_with_path(
                    G,
                    correct_path,
                    output_file_name="{fun_name}_{test_number}".format(
                        fun_name="test_dijkstra_path", test_number=test_nr
                    ),
                    size=8,
                    bgcolor="white",
                    prog="circo",
                )
                # compare correct and test path lengths
                self.assertEqual(
                    correct_path, test_path["path"], "Incorrect dijkstra path"
                )


unittest.main()
