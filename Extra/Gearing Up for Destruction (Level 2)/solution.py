from fractions import Fraction

def solution(pegs):
    n = len(pegs)
    diff = []
    for i in range(n - 1):
        diff.append(pegs[i + 1] - pegs[i])
    summary = sum(diff[::2]) - sum(diff[1::2])
    if n % 2 == 0:
        odd = True
    else:
        odd = False
    if odd is True:
        last_gear = Fraction(summary, 3)
    else:
        last_gear = Fraction(summary, 1)
    possibility = True
    current_value = last_gear
    for i in range(n - 2, -1, -1):
        if current_value < 1:
            possibility = False
            break
        current_value = diff[i] - current_value
    first_gear = last_gear * 2
    if possibility:
        return [first_gear.numerator, first_gear.denominator]
    else:
        return [-1, -1]