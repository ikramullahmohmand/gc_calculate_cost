from flask import Flask, jsonify
import networkx as nx

app = Flask(__name__)

@app.route("/")
def calculate_cost():
    # Load the graphml file
    G = nx.read_graphml("problem.graphml")
    # breakpoint()
    # Get all the edges in the graph
    edges = list(G.edges(data=True))

    # Calculate the cost for Rate Card 1
    cost_1 = 0
    for source, target, data in edges:
        if data['material'] == 'verge':
            cost_1 += int(data['length']) * 2
        elif data['material'] == 'road':
            cost_1 += int(data['length']) * 4

    # Calculate the cost for Rate Card 2
    cost_2 = 0
    for source, target, data in edges:
        if data['material'] == 'verge':
            cost_2 += int(data['length']) * 3
        elif data['material'] == 'road':
            cost_2 += int(data['length']) * 6

    # Return the results as JSON
    return jsonify({"Rate Card 1": cost_1, "Rate Card 2": cost_2})

if __name__ == "__main__":
    app.run(debug=True)
