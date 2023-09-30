def solution(start, length):
    def xor_sequence(n):
        if n % 4 == 0:
            return n
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        return 0

    next_value = start
    break_point = length
    checksum = 0

    while break_point:
        xor_start = xor_sequence(next_value - 1)
        xor_end = xor_sequence(next_value + break_point - 1)
        checksum ^= xor_start ^ xor_end
        next_value += length
        break_point -= 1
    return checksum