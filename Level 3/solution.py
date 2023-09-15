import array
height = 200
def solution(height):
    case = [0,0,1,1,2]
    next_height = 6
    
    def calculate(next_height):
        count = 0
        if next_height%2 == 0:
            count += case[next_height//2-1]
        for i in range (next_height//2+1, next_height):
            count += 1 + case[next_height-i-1]
        return count
        
    while (height >= next_height):
        case.append(calculate(next_height))
        print(next_height, case[next_height-1])
        next_height += 1
        
    return case[height-1]
print(solution(height))