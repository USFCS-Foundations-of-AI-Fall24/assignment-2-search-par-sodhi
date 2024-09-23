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
                # print(ptr)
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
                # print(ptr)
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
#Source I used: https://iq.opengenus.org/depth-limited-search/
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
        next_state, action, depth = search_queue.pop()

        if goal_test(next_state):
            print("Goal found")
            print(f"Goal State: {next_state}")
            print(f"Depth: {depth}")
            ptr = next_state
            while ptr is not None:
                ptr = ptr.prev
                # print(ptr)
            print(f"\nTotal number of states generated: {state_count}")
            return next_state, action
        else:
            # Check if there is a depth limit defined; if not, then just iterate deeply
            if limit is None or depth < limit:
                successors = next_state.successors(action_list)
                # Avoid re-exploring the same state multiple times
                if use_closed_list:
                    filtered_successors = []
                    for s, action_taken in successors:
                        # Check if the state s has not been visited yet
                        if s not in closed_list or closed_list[s] > depth + 1:
                            filtered_successors.append((s, action_taken))
                    # Effectively pruning the search tree to avoid redundant paths
                    successors = filtered_successors
                for s, action_taken in successors:
                    if use_closed_list:
                        closed_list[s] = depth + 1
                    search_queue.append((s, action_taken, depth + 1))
                state_count += len(successors)

    if not goal_found:
        print(f"\nCould not find goal state because depth limit of {limit} was reached.")
        print(f"Total number of states generated: {state_count}")



