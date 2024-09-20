from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    print("Step 1: Initialize the search queue and closed list.")
    search_queue = deque()
    closed_list = {}
    state_count = 0

    print("Step 2: Add the start state to the queue.")
    search_queue.append((startState,""))
    state_count += 1
    if use_closed_list :
        print("Step 3: Add the start state to the closed list.")
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        print("Step 4: Pop the next state from the queue.")
        next_state = search_queue.popleft()
        print(f"Current State: {next_state[0]}\nAction Sequence: {next_state[1]}\n")

        print("Step 5: Check if the current state is the goal state.")
        if goal_test(next_state[0]):
            print("Goal found")
            print(f"Goal State: {next_state}")
            print("\nStep 6: Trace the path back to the start state:")
            #print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"\nTotal number of states generated: {state_count}")
            return next_state
        else :
            print("Step 7: Get successors of the current state.")
            successors = next_state[0].successors(action_list)
            print(f"Successors: {successors}\n")
            if use_closed_list :
                print("Step 8: Filter out successors already in the closed list.")
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    print(f"Adding {s[0]} to closed list.")
                    closed_list[s[0]] = True
            print("Step 9: Add successors to the search queue.")
            search_queue.extend(successors)
            state_count += len(successors)

        print(f"Queue: {list(search_queue)}\n")
        print("=" * 50)
    print("Step 10: Traverse the search queue.")
### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    print("Step 1: Initialize the search stack and closed list.")
    search_queue = deque()
    closed_list = {}
    state_count = 0

    print("Step 2: Add the start state to the stack.")
    search_queue.append((startState,""))
    state_count += 1
    if use_closed_list :
        print("Step 3: Add the start state to the closed list.")
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        print("Step 4: Pop the next state from the stack.")
        next_state = search_queue.pop()
        print(f"Current State: {next_state[0]}\nAction Sequence: {next_state[1]}\n")

        print("Step 5: Check if the current state is the goal state.")
        if goal_test(next_state[0]):
            print("Goal found")
            print(f"Goal State: {next_state}")
            print("\nStep 6: Trace the path back to the start state:")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"\nTotal number of states generated: {state_count}")
            return next_state
        else :
            print("Step 7: Get successors of the current state.")
            successors = next_state[0].successors(action_list)
            print(f"Successors: {successors}\n")
            if use_closed_list :
                print("Step 8: Filter out successors already in the closed list.")
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    print(f"Adding {s[0]} to closed list.")
                    closed_list[s[0]] = True
            print("Step 9: Add successors to the search queue.")
            search_queue.extend(successors)
            state_count += len(successors)
        print(f"Stack: {list(search_queue)}\n")
        print("=" * 50)
    print("Step 10: Traverse the search queue.")
    print(f"\nTotal number of states generated: {state_count}")

## add iterative deepening search here


