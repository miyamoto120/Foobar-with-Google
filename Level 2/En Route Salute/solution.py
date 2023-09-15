def solution(line):
    people = 0
    salute = 0
    reverse = 0
    for direction in line:
        if direction == ">":
            people += 1
        if direction == "<":
            reverse =+ 1
            salute += people * reverse
    return(salute*2)