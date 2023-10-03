def solution(num_buns, num_required):
    # Define a function to calculate factorial
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Calculate combinations using the manual formula
    def combinations(n, r):
        return int(factorial(n) / (factorial(r) * factorial(n - r)))    

    def generate_combinations(items, k):
        if k == 0:
            return [[]]
        if len(items) == 0:
            return []
        head, tail = items[0], items[1:]
        without_head = generate_combinations(tail, k)
        with_head = generate_combinations(tail, k - 1)
        for item in with_head:
            item.append(head)
        return with_head + without_head

    key_count = num_buns - num_required + 1
    max_key_number = combinations(num_buns,num_required - 1)
    result = [[] for _ in range(num_buns)]
    # Generate all combinations of n items taken k at a time without repetition
    combinations = generate_combinations(range(1, num_buns + 1), key_count)
    for i in range(len(combinations)):
        combinations[i].sort()
    combinations.sort()
    
    for i in range(max_key_number):
        for j in combinations[i]:
            result[j - 1].append(i)
    
    return result