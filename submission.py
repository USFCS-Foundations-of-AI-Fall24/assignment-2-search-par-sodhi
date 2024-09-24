from mars_planner import main as rover_main
from mapcoloring import main as mapcoloring_main
from routefinder import main as a_star_main
from mars_planner import problem_decomposition as rover_run_problem_decomposition

if __name__ == "__main__":
    print("Starting Rover Mission Simulation")
    rover_main()

    print("\nStarting Antenna Frequency Assignment")
    mapcoloring_main()

    print("\nStarting A* Search for Mars Pathfinding")
    a_star_main()

    print("\nStarting Rover Mission Problem Decomposition")
    rover_run_problem_decomposition()

