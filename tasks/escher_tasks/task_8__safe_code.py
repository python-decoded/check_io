import re


def safe_code(equation):

    pattern = "-?[#0-9]+[*+-]+[#0-9]+=-?[#0-9]+"
    if not re.fullmatch(pattern, equation):
        return -1

    digits = "0123456789"

    pattern = r"([=+\-*]|^)#[#0-9]"
    if re.search(pattern, equation):
        digits = digits[1:]

    digits = [i for i in digits if i not in equation]

    equation = equation.replace("=", "==")

    for i in digits:
        if eval(equation.replace("#", i)):
            return int(i)

    return -1
