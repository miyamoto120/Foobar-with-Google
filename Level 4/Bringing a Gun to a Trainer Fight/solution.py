from math import atan2

def solution(dimensions, your_position, trainer_position, distance):
    
    column_start = - (distance - your_position[0])//dimensions[0] -1
    column_end = (distance + your_position[0])//dimensions[0]
    row_start = - (distance - your_position[1])//dimensions[1] - 1
    row_end = (distance + your_position[1])//dimensions[1]
    
    hit = dict()
    sqr_distance = distance**2

    for column in range(column_start,column_end + 1):
        for row in range(row_start,row_end + 1):            
            for position in your_position, trainer_position:
                if column == row == 0 and position == your_position:
                    continue                
                mirror_x = dimensions[0]*column + (dimensions[0] - position[0] if column % 2 else position[0]) - your_position[0]
                mirror_y = dimensions[1]*row + (dimensions[1] - position[1] if row % 2 else position[1]) - your_position[1]
                mirror_distance = mirror_x**2 + mirror_y**2                             
                angle = atan2(mirror_x, mirror_y)
                                
                if mirror_distance > sqr_distance or (angle in hit and mirror_distance > abs(hit[angle])):
                    continue
                hit[angle] = mirror_distance * (-1 if position == your_position else 1)

    count = len([1 for angle in hit if hit[angle] > 0])
    return count