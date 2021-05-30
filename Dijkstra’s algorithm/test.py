import networkx as nx
from networkx.generators.harary_graph import hkn_harary_graph
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np
import random
import copy
from networkx.drawing.nx_agraph import graphviz_layout
import unittest
from algorithm.dijkstra import DijkstraSolver


class MyDijkstraImplementationTestCase(unittest.TestCase):
    def setUp(self):
        self.random_seed = 941
        random.seed(self.random_seed)
        self.test_cases_count = 10
        self.test_images_folder = "./test_images"
        nx.graphviz_layout = graphviz_layout

    def generate_new_random_graph(self):
        # generate random vertecies count for the graph
        self.n = random.randint(6, 10)
        # generate random entry and exit nodes for the dijkstra's algorithm
        self.entry_node = 0
        self.exit_node = random.randint(1, self.n - 1)
        # generate new complete graph with self.n vertecies
        self.G = hkn_harary_graph(4, self.n)
        # generate random weights for Graph edges
        for (u, v, w) in self.G.edges(data=True):
            w["weight"] = random.randint(1, 10)
        # create Graph using my implementation of the dijkstra's algorithm
        self.test_G = DijkstraSolver(self.G.copy())

    def draw_graph(self, output_file_name, size=7, bgcolor="white", prog="circo"):
        # draw randomly generated graph for the current test case
        plt.figure(figsize=(size, size))
        ax = plt.axes()
        ax.set_facecolor(bgcolor)
        pos = nx.graphviz_layout(self.G, prog)
        nx.draw_networkx(self.G, pos)
        plt.draw()
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.savefig(
            "{path}/{file_name}.png".format(
                path=self.test_images_folder, file_name=output_file_name
            )
        )
        plt.close()

    def test_dijkstra_path_length(self):
        for test_nr in range(self.test_cases_count):
            self.generate_new_random_graph()
            with self.subTest(i=test_nr):
                # draw currently tested graph
                self.draw_graph(
                    output_file_name="{fun_name}_{test_number}".format(
                        fun_name="test_dijkstra_path_length", test_number=test_nr
                    ),
                    size=7,
                    bgcolor="white",
                    prog="circo",
                )
                # get the correct path length for dijkstra's algorithm
                correct_path_length = nx.dijkstra_path_length(
                    self.G, source=self.entry_node, target=self.exit_node
                )
                # get the dijkstra's path length using my implementation of the algorithm
                test_path_length = self.test_G.get_min_path(
                    src=self.entry_node, dest=self.exit_node
                )["min_dist"]
                # compare correct and test path lengths
                self.assertEqual(
                    correct_path_length,
                    test_path_length,
                    "Incorrect dijkstra path length",
                )

    def test_dijkstra_path(self):
        for test_nr in range(self.test_cases_count):
            self.generate_new_random_graph()
            with self.subTest(i=test_nr):
                # draw currently tested graph
                self.draw_graph(
                    output_file_name="{fun_name}_{test_number}".format(
                        fun_name="test_dijkstra_path", test_number=test_nr
                    ),
                    size=7,
                    bgcolor="white",
                    prog="circo",
                )
                # get the correct path length for dijkstra's algorithm
                correct_path = nx.dijkstra_path(
                    self.G, source=self.entry_node, target=self.exit_node
                )
                # get the dijkstra's path length using my implementation of the algorithm
                test_path = self.test_G.get_min_path(
                    src=self.entry_node, dest=self.exit_node
                )["path"]
                # compare correct and test path lengths
                self.assertEqual(correct_path, test_path, "Incorrect dijkstra path")


unittest.main()
