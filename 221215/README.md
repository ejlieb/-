# 백준 #14600

https://www.acmicpc.net/problem/14600



분할 정복과 구현 두가지 방법으로 풀 수 있을 듯 하다

이 문제의 경우 K <=2 이기 때문에 구현으로 풀이하였으나 만약 K가 커진다면 정사각형을 4분할 하는 방식으로 분할정복 한다.



1. K= 1 크기의 경우 1로 그리드를 채운 후 배수구 자라에만 -1을 넣는다
2. K= 2 크기의 경우 2x2 짜리 정사각형 4개의 경우로 나눈 뒤, 중앙 자리에 배수구인 경우, 그 외 경우로 나누어 구현한다.

```python
K = int(input())
hole_x, hole_y = list(map(int, input().split()))
if K == 1:
    grid = [[1,1],[1,1]]
else:
    grid = [[1,1,2,2],[1,5,5,2],[3,5,5,4],[3,3,4,4]]


def divide(target_x, target_y, grid):
    if target_y <= 2 and target_x <= 2:
        if grid[target_y - 1][target_x - 1] == 5:
            grid[target_y - 1][target_x - 1] = -1
        else:
            grid[target_y - 1][target_x - 1] = -1
            grid[1][1] = 1
    elif target_y <= 2 and target_x > 2:
        if grid[target_y - 1][target_x - 1] == 5:
            grid[target_y - 1][target_x - 1] = -1
        else:
            grid[target_y - 1][target_x - 1] = -1
            grid[1][2] = 2
    elif target_y > 2 and target_x <= 2:
        if grid[target_y - 1][target_x - 1] == 5:
            grid[target_y - 1][target_x - 1] = -1
        else:
            grid[target_y - 1][target_x - 1] = -1
            grid[2][1] = 3
    else:
        if grid[target_y - 1][target_x - 1] == 5:
            grid[target_y - 1][target_x - 1] = -1
        else:
            grid[target_y - 1][target_x - 1] = -1
            grid[2][2] = 4



if K == 2:
    divide(hole_x, hole_y, grid)
else:
    grid[hole_y - 1][hole_x - 1] = -1

for line in grid[::-1]:
    for tile in line:
        print(tile, end=' ')
    print('')
```

