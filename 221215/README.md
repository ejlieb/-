# 백준 #21870

https://www.acmicpc.net/problem/21870



최대공약수 함수와 분할정복을 통해서 푸는 문제

주어진 자취방 배열 S를 len(S) // 2한 mid를 기준으로 왼쪽 리스트를 선택하여 최대공약수를 구하는 것과, 오른쪽 리스트를 선택하여 최대공약수를 구하는 것 중 최대값을 선택하여 리턴한다.

```python
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
```

