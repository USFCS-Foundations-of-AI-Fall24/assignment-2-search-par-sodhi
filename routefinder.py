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

# Source I used to help with implementation: https://www.geeksforgeeks.org/a-search-algorithm/
def a_star(start_state, h_value, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = set() if use_closed_list else None
    search_queue.put((start_state.f, start_state))
    state_count = 0
    map_p = {start_state: None}

    while not search_queue.empty():
        current_state = search_queue.get()[1]
        state_count += 1
        if current_state.is_goal():
            print(f"Goal reached: {current_state.location}")
            return display_path(current_state, map_p), state_count

        if use_closed_list and current_state.location in closed_list:
            continue
        closed_list.add(current_state.location)
        mars_graph = current_state.mars_graph
        edges = mars_graph.get_edges(current_state.location)

        for edge in edges:
            next_state = map_state(location=edge.dest, mars_graph=current_state.mars_graph, prev_state=current_state, g=current_state.g + edge.val)
            next_state.h = h_value(next_state)
            next_state.f = next_state.g + next_state.h
            if use_closed_list and next_state.location in closed_list:
                continue
            search_queue.put((next_state.f, next_state))
            map_p[next_state] = current_state
    print("Cannot find route.")
    return None, state_count

def display_path(goal_state, parent_map):
    path = []
    current = goal_state
    while current is not None:
        path.append(current.location)
        current = parent_map[current]
    path.reverse()
    return path

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    goal = "1,1"
    a1, b1 = map(int, state.location.split(','))
    a2, b2 = map(int, goal.split(","))
    # print(f"Calculating SLD from {state.location} to {goal}: {math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)}")
    return math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            if line:
                current_node, locations = parse_line(line)
                if current_node not in graph.g:
                    graph.add_node(current_node)
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
                # print(f"Added new node: {current_location}")
            graph.add_edge(Edge(current_node, current_location, 1))
            # print(f"Added edge from {current_node} to {current_location} with default weight 1")
        index += 1


def main():
    filename = "marsmap.txt"
    try:
        print(f"Mars graph creating from {filename}")
        mars_graph = read_mars_graph(filename)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the Mars graph: {e}")
        return

    start_state = map_state(location="8,8", mars_graph=mars_graph, g=0)

    print("\nRunning A* Search with SLD:")
    try:
        answer_generated_a_star, states_generated_a_star = a_star(start_state, sld)
        print("A* Search Result:", answer_generated_a_star)
        print(f"States by A* with SLD: {states_generated_a_star}")
    except Exception as e:
        print(f"An error occurred during A* search with SLD heuristic: {e}")

    print("\nRunning Uniform Cost Search:")
    try:
        answer_generated_uniform, states_generated_uniform = a_star(start_state, h1)
        print("Uniform Search Result:", answer_generated_uniform)
        print(f"States by UCS: {states_generated_uniform}")
    except Exception as e:
        print(f"An error occurred during Uniform Cost Search: {e}")

if __name__ == "__main__":
    main()
