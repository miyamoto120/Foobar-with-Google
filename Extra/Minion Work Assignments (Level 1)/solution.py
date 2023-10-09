def solution(data, n):
    # Count occurrences of each number in the input list
    num_counts = {}
    for num in data:
        num_counts[num] = num_counts.get(num, 0) + 1

    # Create a new list with numbers that occur less than or equal to n times
    result = [num for num in data if num_counts[num] <= n]
    return result