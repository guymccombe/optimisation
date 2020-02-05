import pulp

if __name__ == "__main__":
    # Problem declaration
    problem = pulp.LpProblem(name="LuggagePacking", sense=pulp.LpMaximize)

    # Variable declaration
    A = pulp.LpVariable("A", lowBound=0, cat="Binary")
    B = pulp.LpVariable("B", lowBound=0, cat="Binary")
    C = pulp.LpVariable("C", lowBound=0, cat="Binary")
    D = pulp.LpVariable("D", lowBound=0, cat="Binary")
    E = pulp.LpVariable("E", lowBound=0, cat="Binary")
    F = pulp.LpVariable("F", lowBound=0, cat="Binary")

    # Objective function
    problem += 60*A + 70*B + 40*C + 70*D + 16*E + 100*F, "Value"

    # Constraints
    problem += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20
    problem += C - D <= 0

    # Problem solution
    problem.solve()
    print(problem)
    print(pulp.LpStatus[problem.status])

    for variable in problem.variables():
        print(f"{variable.name}: {variable.varValue}" )
    print(f"Total value of luggage: {pulp.value(problem.objective)}")
