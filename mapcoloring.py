from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

A1 = model.NewIntVar(0, 2, "Antenna 1")
A2 = model.NewIntVar(0, 2, "Antenna 2")
A3 = model.NewIntVar(0, 2, "Antenna 3")
A4 = model.NewIntVar(0, 2, "Antenna 4")
A5 = model.NewIntVar(0, 2, "Antenna 5")
A6 = model.NewIntVar(0, 2, "Antenna 6")
A7 = model.NewIntVar(0, 2, "Antenna 7")
A8 = model.NewIntVar(0, 2, "Antenna 8")
A9 = model.NewIntVar(0, 2, "Antenna 9")

model.Add(A1 != A2)
model.Add(A1 != A3)
model.Add(A1 != A4)
model.Add(A2 != A1)
model.Add(A2 != A3)
model.Add(A2 != A5)
model.Add(A2 != A6)
model.Add(A3 != A1)
model.Add(A3 != A2)
model.Add(A3 != A6)
model.Add(A3 != A9)
model.Add(A4 != A1)
model.Add(A4 != A2)
model.Add(A4 != A5)
model.Add(A5 != A2)
model.Add(A5 != A4)
model.Add(A6 != A2)
model.Add(A6 != A7)
model.Add(A6 != A8)
model.Add(A7 != A6)
model.Add(A7 != A8)
model.Add(A8 != A7)
model.Add(A8 != A9)
model.Add(A9 != A3)
model.Add(A9 != A8)

## Solver
status = solver.Solve(model)

# Output results if solution found
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Frequency assignment:')
    print(f'Antenna 1: Frequency {solver.Value(A1)+1}')
    print(f'Antenna 2: Frequency {solver.Value(A2)+1}')
    print(f'Antenna 3: Frequency {solver.Value(A3)+1}')
    print(f'Antenna 4: Frequency {solver.Value(A4)+1}')
    print(f'Antenna 5: Frequency {solver.Value(A5)+1}')
    print(f'Antenna 6: Frequency {solver.Value(A6)+1}')
    print(f'Antenna 7: Frequency {solver.Value(A7)+1}')
    print(f'Antenna 8: Frequency {solver.Value(A8)+1}')
    print(f'Antenna 9: Frequency {solver.Value(A9)+1}')
else:
    print('No solution found.')


