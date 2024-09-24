## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search, depth_limited_search


class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False,holding_tool=False, charged=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.holding_tool = holding_tool
        self.charged=charged
        self.prev = None

    ## you do this.
    def __eq__(self, other):
        if not isinstance(other, RoverState):
            return NotImplemented
        return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.holding_tool == other.holding_tool and
                self.charged == other.charged)


    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Holding Tool?: {self.holding_tool}\n" +
                f"Charged? {self.charged}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev = state
    return r2
def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here
def pick_up_tool(state):
    if not state.holding_tool:
        r2 = deepcopy(state)
        r2.holding_tool = True
        r2.prev = state
        return r2
    return state

def drop_tool(state):
    if state.holding_tool:
        r2 = deepcopy(state)
        r2.holding_tool = False
        r2.prev = state
        return r2
    return state

def use_tool(state):
    if state.loc == "sample" and state.holding_tool and not state.sample_extracted:
        r2 = deepcopy(state)
        r2.sample_extracted = True
        r2.prev = state
        return r2
    return state

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample,pick_up_sample, move_to_sample, move_to_battery,
               move_to_station, pick_up_tool, drop_tool, use_tool]

def battery_goal(state) :
    return state.loc == "battery"

def move_to_sample(state):
    return state.loc == "sample" and state.holding_tool == True and state.sample_extracted == False and state.holding_sample == False

def remove_sample(state):
    return state.sample_extracted and state.holding_sample == True and state.holding_tool == True and state.loc == "sample"

## add your goals here.
#Mission Complete Function done
def mission_complete(state):
    if state.loc == "battery" and state.charged == True and state.sample_extracted == True and state.holding_sample == False and state.holding_tool == False:
        print("-" * 50)
        print("The Mission Has Been Completed")
        print("-" * 50)
        return True
    return False


def problem_decomposition():
    initial_state = RoverState()

    print("Problem 1: Move to Sample(Breadth First Search)")
    print(breadth_first_search(initial_state, action_list, move_to_sample))
    print("\nProblem 1: Move to Sample(Depth First Search)")
    print(depth_first_search(initial_state, action_list, move_to_sample))
    print("\nProblem 1: Move to Sample(Depth Limited Search)")
    print(depth_limited_search(initial_state, action_list, move_to_sample,limit=7))

    sample_location_state = RoverState(loc="sample", holding_tool=True)
    print("\nProblem 2: Remove Sample(Breadth First Search)")
    print(breadth_first_search(sample_location_state, action_list, remove_sample))
    print("\nProblem 2: Remove Sample(Depth First Search)")
    print(depth_first_search(sample_location_state, action_list, remove_sample))
    print("\nProblem 2: Remove Sample(Depth Limited Search)")
    print(depth_limited_search(sample_location_state, action_list, remove_sample, limit =7))

    sample_extracted_state = RoverState(loc="sample", sample_extracted=True, holding_sample=True)
    print("\nProblem 3: Return to Charger(Breadth First Search)")
    print(breadth_first_search(sample_extracted_state, action_list, battery_goal))
    print("\nProblem 3: Return to Charger(Depth First Search)")
    print(depth_first_search(sample_extracted_state, action_list, battery_goal))
    print("\nProblem 3: Return to Charger(Depth Limited Search)")
    print(depth_limited_search(sample_extracted_state, action_list, battery_goal, limit=7))

def main():
    s = RoverState()
    print("Initial State\n", s)
    print("\n")
    print("Breadth First Search\n")
    print(breadth_first_search(s, action_list, mission_complete))
    print("\n")
    print("Depth First Search\n")
    print(depth_first_search(s, action_list, mission_complete))
    print("\n")
    print("Depth Limited Search\n")
    print(depth_limited_search(s, action_list, mission_complete, limit=7))
    print("\n")

if __name__=="__main__" :
    main()



