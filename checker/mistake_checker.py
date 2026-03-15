def detect_mistakes(eq):

    mistakes = []

    if "+-" in eq:
        mistakes.append("Possible sign mistake detected.")

    if "==" in eq:
        mistakes.append("Double equal sign detected.")

    if "(" in eq and ")" not in eq:
        mistakes.append("Missing closing bracket.")

    return mistakes