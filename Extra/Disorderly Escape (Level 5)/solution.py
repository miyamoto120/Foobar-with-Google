def solution(w, h, s):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
        
    def Counter(iterable):
        count_dict = {}
        for item in iterable:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        return count_dict

    def gcd(a,b):
        while b:
            a, b = b, a % b
        return a

    def partition(n, m=None):
        if m is None:
            m = n
        if n == 0:
            return [[]]
        if n < 0 or m == 0:
            return []
        
        partitions = []
        for i in range(min(n, m), 0, -1):
            sub_partitions = partition(n - i, i)
            for sub_partition in sub_partitions:
                partitions.append([i] + sub_partition)
        
        return partitions

    def cy(y,n):
        counted_y = Counter(y)
        unique_y = list(set(y))
        conjugacy = factorial(n)
        for i in unique_y:
            conjugacy //= ((i**counted_y[i])*factorial(counted_y[i]))
        return conjugacy

    partition_w = partition(w)
    partition_h = partition(h)
    total = 0
    for part_w in partition_w:
        for part_h in partition_h:
            cy1 = cy(part_w,w)
            cy2 = cy(part_h,h)
            exp_sum = 0
            for y1 in part_w:
                for y2 in part_h:
                    exp_sum += gcd(y1,y2)
            total += cy1*cy2*(s**exp_sum)

    return str(total//(factorial(w)*factorial(h)))

