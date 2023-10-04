from fractions import Fraction

def solution(pegs):
    n = len(pegs)
    diff = []
    for i in range(n - 1):
        diff.append(pegs[i + 1] - pegs[i])
    odd = True
    sum = diff[0]
    for i in range(1, n - 1):
        odd = not odd
        if odd == False:
            sum -= diff[i]
        else:
            sum += diff[i]
    if odd is True:
        last_gear = Fraction(sum * 2, 3)
    else:
        last_gear = Fraction(sum * 2, 1)
    possibility = True
    current_value = last_gear
    for i in range(n - 2, -1, -1):
        if current_value < 0:
            possibility = False
            break
        current_value = diff[i] - current_value
    if possibility:
        return (last_gear.numerator, last_gear.denominator)
    else:
        return (-1, -1)

print(solution([4, 17, 50]))
print(solution([4, 30, 50]))
