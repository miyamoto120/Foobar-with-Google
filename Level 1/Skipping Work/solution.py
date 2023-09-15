def solution(a, b):
    if len(a) > len (b):
        print(sum(a) - sum(b))
        return(sum(a) - sum(b))
    else:
        print(sum(b) - sum(a))
        return(sum(b) - sum(a))