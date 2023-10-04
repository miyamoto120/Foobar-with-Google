from fractions import Fraction
import numpy as np

def solution(m):
    # Function to calculate GCD
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Function to calculate LCM using GCD
    def lcm(a, b):
        return a * b // gcd(a, b)

    if len(m) < 2:
        return [1,1]

    n = len(m)
    # Split matrix, find R, Q
    terminal = []
    non_terminal = []
    for i in range(n):
        if sum(m[i]) - m[i][i] == 0:
            terminal.append(i)
        else:
            non_terminal.append(i)
    r = []
    q = []
    for i in non_terminal:
        summary = sum(m[i])
        temp_matrix = []
        for j in terminal:
            temp_matrix.append(Fraction(m[i][j], summary))
        r.append(temp_matrix)
        temp_matrix = []
        for j in non_terminal:
            temp_matrix.append(Fraction(m[i][j], summary))
        q.append(temp_matrix)

    R = np.array(r)
    Q = np.array(q)
    I = np.eye(len(Q), dtype=Fraction)
    temp = I - Q
    # Convert Fraction elements to float for the computation
    array_float = np.array([[float(elem) for elem in row] for row in temp])
    # Calculate the inverse of the array (as float)
    inverse_array_float = np.linalg.inv(array_float)
    # Convert the result back to Fraction
    F = np.array([[Fraction(elem).limit_denominator() for elem in row] for row in inverse_array_float])
    FR = np.dot(F, R)
    # Initialize variables
    denominators = []
    numerators = []
    # Iterate through the Fraction objects in the array
    for i in FR[0]:
        denominators.append(i.denominator)
    lcm_result = denominators[0]
    for num in denominators[1:]:
        lcm_result = lcm(lcm_result, num)
    for i in FR[0]:
        numerators.append(i.numerator * lcm_result // i.denominator)
    # Append the summary to the numerators list
    result = numerators + [lcm_result]
    return result