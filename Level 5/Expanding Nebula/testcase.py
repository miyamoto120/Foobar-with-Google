from solution import solution

g1 = [[True, True, False, True, False, True, False, True, True, False],
      [True, True, False, False, False, False, True, True, True, False],
      [True, True, False, False, False, False, False, False, False, True],
      [False, True, False, False, False, False, True, True, False, False]]
g2 = [[True, False, True], [False, True, False], [True, False, True]]
g3 = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False],
      [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False],
      [True, False, True, False, False, True, True, True]]
g4 = [
    [True, True, True, True, True, True, False, True, False, False, False, True, True, True, False, False, True, False,
     False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, True, True,
     True, False, False, False, True, True, True, True, False, True, True, True],
    [False, False, False, False, True, True, False, True, True, False, True, True, False, False, False, True, True,
     True, True, True, True, True, False, False, False, True, True, False, False, True, False, False, False, True,
     False, False, False, True, False, False, True, True, False, True, True, True, False, True],
    [False, False, False, True, False, False, True, True, True, False, False, False, False, False, False, True, True,
     True, False, False, False, True, False, True, False, True, False, False, True, True, True, False, True, False,
     False, True, True, True, True, False, False, True, False, False, True, True, True, True],
    [True, False, True, True, False, False, True, False, True, True, True, True, True, True, False, False, False, False,
     False, True, True, True, True, False, False, True, False, False, True, False, True, False, True, True, True, True,
     True, False, False, True, True, True, True, False, False, True, False, True],
    [False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, True,
     True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True,
     False, False, True, False, False, False, True, False, False, False, False, False, False],
    [False, False, False, True, False, True, True, True, True, False, True, True, False, True, True, False, False,
     False, True, True, True, False, True, True, True, True, False, True, False, False, True, False, False, False,
     False, True, False, False, True, False, True, False, False, False, True, True, True, True],
    [False, False, True, True, True, False, True, False, True, True, True, False, True, True, True, True, False, True,
     True, True, False, True, False, True, False, False, False, True, True, True, True, False, False, True, True, False,
     True, True, True, True, False, False, True, False, False, False, True, True],
    [False, True, True, False, False, False, True, False, False, False, True, True, True, False, False, True, False,
     False, False, True, True, False, False, True, True, True, False, True, False, True, True, False, False, False,
     False, False, True, True, False, True, False, True, False, False, False, True, False, True],
    [False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, True, True, False,
     False, True, False, False, False, True, True, True, False, False, False, True, True, False, True, False, True,
     False, True, True, True, True, True, False, True, True, False, False, True, True]]
g5 = [
    [True, True, True, True, True, True, False, True, False, False, False, True, True, True],
    [False, False, False, False, True, True, False, True, True, False, True, True, False, False],
    [False, False, False, True, False, False, True, True, True, False, False, False, False, False],
    [True, False, True, True, False, False, True, False, True, True, True, True, True, True],
    [False, False, False, False, False, False, False, True, True, False, False, False, False, False],
    [False, False, False, True, False, True, True, True, True, False, True, True, False, True],
    [False, False, True, True, True, False, True, False, True, True, True, False, True, True],
    [False, True, True, False, False, False, True, False, False, False, True, True, True, False],
    [False, True, False, True, True, False, True, False, True, False, False, True, True, False]
]
g6 = [
    [True, True, True, True, True, True, False, True, False, False, False, True, True, True],
    [False, False, False, False, True, True, False, True, True, False, True, True, False, False],
    [False, False, False, True, False, False, True, True, True, False, False, False, False, False],
    [True, False, True, True, False, False, True, False, True, True, True, True, True, True],
    [False, False, False, False, False, False, False, True, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, True, True, False, False, False, False, False],
]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
print(solution(g5))
print(solution(g6))
print("done")