import unittest
import networkx as nx
from GC_task.app import app

class TestCostCalculation(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_calculate_cost(self):
        # Load the graphml file
        G = nx.read_graphml("problem.graphml")

        # Get all the edges in the graph
        edges = list(G.edges(data=True))

        # Calculate the expected cost for Rate Card 1
        expected_cost_1 = 0
        for source, target, data in edges:
            if data['material'] == 'verge':
                expected_cost_1 += int(data['length']) * 2
            elif data['material'] == 'road':
                expected_cost_1 += int(data['length']) * 4

        # Calculate the expected cost for Rate Card 2
        expected_cost_2 = 0
        for source, target, data in edges:
            if data['material'] == 'verge':
                expected_cost_2 += int(data['length']) * 3
            elif data['material'] == 'road':
                expected_cost_2 += int(data['length']) * 6

        # Make a request to the Flask application
        response = self.app.get("/")
        data = response.get_json()

        # Verify that the response contains the expected cost for Rate Card 1
        self.assertEqual(data["Rate Card 1"], expected_cost_1)

        # Verify that the response contains the expected cost for Rate Card 2
        self.assertEqual(data["Rate Card 2"], expected_cost_2)

if __name__ == '__main__':
    unittest.main()
