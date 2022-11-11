def operate(sign, *args):
    if sign in ("+", "-"):
        result = 0
    else:
        result = 1
        
    if sign == "+":
        for el in args:
            result += el
    elif sign == "-":
        for el in args:
            result -= el
    elif sign == "*":
        for el in args:
            result *= el
    elif sign == "/":
        for el in args:
            result /= el

    return result
