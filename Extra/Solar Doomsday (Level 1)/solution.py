def solution(area):
    size = 1
    square_size = [1]
    result = []
    while square_size[size - 1] <= area:
        size += 1
        square_size.append(size**2)
    size -= 2
    while area > 0:
        if area < square_size[size]:
            size -= 1
            continue
        area -= square_size[size]
        result.append(square_size[size])
    return result