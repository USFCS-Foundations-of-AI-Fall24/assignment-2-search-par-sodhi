from mars_planner import main as rover_main
from mapcoloring import main as ortools_main
from routefinder import main as a_star_main
from mars_planner import problem_decomposition as rover_run_problem_decompositon

if __name__ == "__main__":
    print("Starting Rover Mission Simulation")
    rover_main()

    print("\nStarting Antenna Frequency Assignment")
    ortools_main()

    print("\nStarting A* Search for Mars Pathfinding")
    a_star_main()

    print("\nStarting Rover Mission Subproblem")
    rover_run_problem_decompositon()

