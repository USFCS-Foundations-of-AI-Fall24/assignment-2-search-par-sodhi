from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    state_count += 1
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()

        if goal_test(next_state[0]):
            print("Goal found")
            print(f"Goal State: {next_state}")
            #print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"\nTotal number of states generated: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            print(f"Successors: {successors}\n")
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            state_count += len(successors)

    print(f"\nTotal number of states generated: {state_count}")
### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    state_count += 1
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()

        if goal_test(next_state[0]):
            print("Goal found")
            print(f"Goal State: {next_state}")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"\nTotal number of states generated: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            state_count += len(successors)
    print(f"\nTotal number of states generated: {state_count}")

## add iterative deepening search here

def depth_limited_search(startState, action_list, goal_test, use_closed_list=True, limit=None):
    search_queue = deque()
    closed_list = {}
    state_count = 0
    goal_found = False

    search_queue.append((startState, "", 0))
    state_count += 1
    if use_closed_list:
        closed_list[startState] = True

    while len(search_queue) > 0:
        next_state, action_sequence, depth = search_queue.pop()

        if goal_test(next_state):
            print("Goal found")
            print(f"Goal State: {next_state}, Action Sequence: {action_sequence}, Depth: {depth}")
            ptr = next_state
            while ptr is not None:
                print(ptr)
                ptr = ptr.prev
            print(f"\nTotal number of states generated: {state_count}")
            return next_state, action_sequence, depth

        if limit is not None and depth >= limit:
            print(f"Depth limit reached at depth {depth}, not expanding this node further.")
            continue

        successors = next_state.successors(action_list)
        if use_closed_list:
            successors = [item for item in successors if item[0] not in closed_list]
            for s in successors:
                closed_list[s[0]] = True

        for s in successors:
            search_queue.append((s[0], action_sequence + " -> " + s[1], depth + 1))
            state_count += 1

    if not goal_found:
        print(f"\nCould not find goal state because depth limit of {limit} was reached.")
        print(f"Total number of states generated: {state_count}")


