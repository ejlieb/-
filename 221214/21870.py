from math import gcd
N = int(input())
rooms = list(map(int, input().split()))


def divide(lst):
    mid = len(lst) // 2
    if len(lst) == 2:
        return sum(lst)
    elif len(lst) == 1:
        return lst[0]

    return max(divide(lst[mid:]) + gcd(*lst[:mid]), divide(lst[:mid]) + gcd(*lst[mid:]))




print(divide(rooms))