import math
from queue import PriorityQueue

from Graph import Edge, Graph


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,filename=None,prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h
        if filename:
            self.mars_graph = read_mars_graph(filename)


    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    sqt(a^ + b2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()
    print("Initializing new graph object.")
    with open(filename, 'r') as file:
        for line in file:
            if line:
                current_node, locations = parse_line(line)
                if current_node not in graph.g:
                    graph.add_node(current_node)
                    print(f"Added new node: {current_node}")
                process_locations(current_node, locations, graph)
    print("Graph loading complete.")
    return graph

def parse_line(line):
    parts = line.split(':')
    src = parts[0].strip()
    if len(parts) > 1:
        locations = parts[1].strip().split()
    else:
        locations = []
    return src, locations

def process_locations(current_node, locations, graph):
    index = 0
    while index < len(locations):
        current_location = locations[index].strip()
        if current_location:
            if current_location not in graph.g:
                graph.add_node(current_location)
                print(f"Added new node: {current_location}")
            graph.add_edge(Edge(current_node, current_location, 1))
            print(f"Added edge from {current_node} to {current_location} with default weight 1")
        index += 1


def main():
    filename = "marsmap.txt"
    try:
        print("Loading the Mars graph from a TXT file...")
        mars_graph = read_mars_graph(filename)
        print(mars_graph)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the Mars graph: {e}")
        return

if __name__ == "__main__":
    main()
