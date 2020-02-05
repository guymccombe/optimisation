import pulp

if __name__ == "__main__":
    # Problem declaration
    problem = pulp.LpProblem(name="PaintMixing", sense=pulp.LpMaximize)

    # Variable declaration
    red = pulp.LpVariable("red", lowBound=0, cat="Continuous")
    green = pulp.LpVariable("green", lowBound=0, cat="Continuous")
    blue = pulp.LpVariable("blue", lowBound=0, cat="Continuous")
    black = pulp.LpVariable("black", lowBound=0, cat="Continuous")

    # Objective function
    problem += 10*red + 15*green + 25*blue + 25*black, "Profit"

    # Constraints
    problem += 1/2*red + 1/2*blue + 1/3*black <= 5
    problem += 1/2*green + 1/2*blue + 1/3*black <= 10
    problem += 1/2*red + 1/2*green + 1/3*black <= 11

    # Problem solution
    problem.solve()
    print(problem)
    print(pulp.LpStatus[problem.status])

    for variable in problem.variables():
        print(f"{variable.name}: {variable.varValue}" )
    print(f"Total profit: {pulp.value(problem.objective)}")
    