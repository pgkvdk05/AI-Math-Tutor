import sympy as sp
import re


def normalize_equation(eq):
    """
    Convert OCR math text into SymPy friendly format
    """

    eq = eq.replace("^", "**")

    # Convert 3x -> 3*x
    eq = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)

    # Convert x2 -> x*2 (rare OCR case)
    eq = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', eq)

    return eq


def solve_equation(eq):

    x = sp.symbols('x')

    eq = normalize_equation(eq)

    left, right = eq.split("=")

    expr = sp.sympify(left) - sp.sympify(right)

    solution = sp.solve(expr, x)

    return solution