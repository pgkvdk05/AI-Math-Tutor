from solver.equation_solver import solve_equation

test_cases = [
    "3x + 5 = 14",
    "2x - 6 = 10",
]


def run():

    for eq in test_cases:

        print("Equation:", eq)

        print("Solution:", solve_equation(eq))

        print()