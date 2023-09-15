def solution(l,t):
    for i in range(0,len(l)):
        count = 0
        for j in range (i,len(l)):
            count += l[j]
            if count == t:
                return (i,j)
    return(-1,-1)