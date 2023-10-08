def solution(l):
    def output(m):
        if m == []:
            return 0
        m.sort(reverse=True)
        return int(''.join(map(str, m)))

    remainder = sum(l) % 3

    # If the sum is already divisible by 3, return the sorted number
    if remainder == 0:
        return output(l)

    # Try removing one digit
    for i in range(10):
        if i in l and i % 3 == remainder:
            l.remove(i)
            return output(l)

    # Try removing two digits
    smallest_sums = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if (l[i] + l[j]) % 3 == remainder:
                smallest_sums.append([l[i], l[j]])

    if smallest_sums:
        # Find the smallest number formed by removing two digits
        smallest_sums.sort(key=lambda x: x[0] + x[1])
        l.remove(smallest_sums[0][0])
        l.remove(smallest_sums[0][1])
        return output(l)

    # If no valid numbers can be formed, return 0
    return 0