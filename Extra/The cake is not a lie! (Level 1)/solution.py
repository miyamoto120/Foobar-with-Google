def solution(s):
    length = len(s)
    max_parts = 1

    # Find all factors of the length of the input string
    for i in range(1, length + 1):
        if length % i == 0:
            # Check if the string can be divided into equal parts of length i
            if all(s[j] == s[j % i] for j in range(length)):
                max_parts = max(max_parts, length // i)

    return max_parts