def solution(n, b):
    def subtract_in_base_b(num1, num2):
        result = []
        # Ensure the numbers have the same length by adding leading zeros
        while len(num2) < leng:
            num2 = [0] + num2

        flag = 0
        # Perform subtraction from right to left
        for i in range(leng - 1, -1, -1):
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
    n = tuple(map(int, n))
    leng = len(n)
    seen = dict()
    cycle_length = 0
    next_value = n

    while True:
        # Calculate x and y as described in the algorithm
        x = sorted(next_value, reverse=True)
        y = sorted(next_value)
        if str(next_value) in seen:
            break
        seen[str(next_value)] = cycle_length
        seen[str(x)] = cycle_length
        seen[str(y)] = cycle_length
        next_value = subtract_in_base_b(x, y)
        next_value = tuple(next_value)  # Convert next_value back to a tuple
        cycle_length += 1

    # Length of the cycle is the difference between the current cycle length and the previous index where n is seen
    return cycle_length - seen[str(next_value)]