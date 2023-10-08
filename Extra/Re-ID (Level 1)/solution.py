def solution(i):
    prime = [2]
    next_value = 3
    prime_len = 1
    end_index = i + 5
    while end_index > prime_len:
        isPrime = True
        for j in prime:
            if next_value % j == 0:
                isPrime = False
        if isPrime:
            prime.append(next_value)
            prime_len += len(str(next_value))
        next_value += 1
    array_as_string = ''.join(map(str, prime))
    return array_as_string[i:i+5]