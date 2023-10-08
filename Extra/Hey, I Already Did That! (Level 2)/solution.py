def solution(n, b):
    def subtract_in_base_b(num1, num2, b):
        result = []
        # Ensure the numbers have the same length by adding leading zeros    
        while len(num2) < n:
            num2 = [0] + num2
        
        flag = 0
        # Perform subtraction from right to left
        for i in range(n - 1, -1, -1):
            # Subtract digits
            digit = num1[i] - flag - num2[i]
            # If the result is negative, add base (3) to the digit and set the borrow flag
            if digit < 0:
                digit += b
                flag = 1
            else:
                flag = 0
            result.insert(0, digit)
        
        return result
    # Convert n from base b to a list of integers
    n = len(n)
    seen = dict()
    cycle_length = 0
    
    while seen[] not in seen:
        seen[tuple(n)] = cycle_length        
        # Calculate x and y as described in the algorithm
        x = sorted(n, reverse=True)
        y = sorted(n)
        subtract_in_base_b(x, y, b)
        cycle_length += 1
    
    # Length of the cycle is the difference between the current cycle length and the previous index where n is seen
    return cycle_length - seen[tuple(n)]

# Example usage
print(solution("210022", 3))  # Output: 3
print(solution("1211", 10))  # Output: 1
