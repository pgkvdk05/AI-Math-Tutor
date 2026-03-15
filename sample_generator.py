import random

equations = [
    "3x + 5 = 14",
    "2x - 6 = 10",
    "x^2 - 5x + 6 = 0",
    "4x + 8 = 0"
]


def generate():

    return random.choice(equations)


if __name__ == "__main__":

    print(generate())