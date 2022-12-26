# 백준 #21870

https://www.acmicpc.net/problem/21870

1. BFS를 통해서 한 알파벳이 어디까지 이어지는 지 체크
2. BFS를 돌리면서 알파벳으로 이루어진 영역의 최소, 최대 x, y좌표를 체크한 후 BFS가 종료되면 최소x,y부터 최대 x,y사이의 직사각형 영역에 다른 알파벳이 있나 체크



! BFS를 사용하지 않고 2x2사이즈에서 한 자리만 다른 알파벳인 경우를 이중 for 문으로 순회하면서 찾아줘도 된다.

모든 직사각형이 아닌 경우는 2x2사이즈에서 3개만 같은 알파벳이고 1개가 다를 때 발생하기 때문

```python
from collections import deque

N, M = list(map(int, input().split()))
grid = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = False
num = 1
breakflag = True


def bfs(sp, alph, num):
    global visited, grid
    min_x = sp[0]
    min_y = sp[1]
    max_x = sp[0]
    max_y = sp[1]
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    queue = deque()
    visited[sp[0]][sp[1]] = num
    queue.append(sp)
    while queue:
        t = queue.popleft()
        for m in range(4):
            new_x = t[0] + nx[m]
            new_y = t[1] + ny[m]
            if 0 <= new_x < N and 0 <= new_y < M:
                if visited[new_x][new_y] == 0 and grid[new_x][new_y] == alph:
                    queue.append((new_x,new_y))
                    visited[new_x][new_y] = num
                    if new_x > max_x:
                        max_x = new_x
                    if new_y > max_y:
                        max_y = new_y
                    if new_x < min_x:
                        mix_x = new_x
                    if new_y < min_y:
                        min_y = new_y
        if not queue:
            for i in range(min_x, max_x + 1):
                for j in range(min_y, max_y + 1):
                    if grid[i][j] != alph:
                        return False
            return True

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if bfs((i,j), grid[i][j], num) == False:
                breakflag = False
                print('BaboBabo')
                break
            num += 1
    if breakflag == False:
        break
else:
    print('dd')xxxxxxxxxx from math import gcdN = int(input())rooms = list(map(int, input().split()))def divide(lst):    mid = len(lst) // 2    if len(lst) == 2:        return sum(lst)    elif len(lst) == 1:        return lst[0]    return max(divide(lst[mid:]) + gcd(*lst[:mid]), divide(lst[:mid]) + gcd(*lst[mid:]))from collections import dequeN, M = list(map(int, input().split()))grid = [list(input()) for _ in range(N)]visited = [[0] * M for _ in range(N)]answer = Falsenum = 1breakflag = Truedef bfs(sp, alph, num):    global visited, grid    min_x = sp[0]    min_y = sp[1]    max_x = sp[0]    max_y = sp[1]    nx = [0,0,1,-1]    ny = [1,-1,0,0]    queue = deque()    visited[sp[0]][sp[1]] = num    queue.append(sp)    while queue:        t = queue.popleft()        for m in range(4):            new_x = t[0] + nx[m]            new_y = t[1] + ny[m]            if 0 <= new_x < N and 0 <= new_y < M:                if visited[new_x][new_y] == 0 and grid[new_x][new_y] == alph:                    queue.append((new_x,new_y))                    visited[new_x][new_y] = num                    if new_x > max_x:                        max_x = new_x                    if new_y > max_y:                        max_y = new_y                    if new_x < min_x:                        mix_x = new_x                    if new_y < min_y:                        min_y = new_y        if not queue:            for i in range(min_x, max_x + 1):                for j in range(min_y, max_y + 1):                    if grid[i][j] != alph:                        return False            return Truefor i in range(N):    for j in range(M):        if visited[i][j] == 0:            if bfs((i,j), grid[i][j], num) == False:                breakflag = False                print('BaboBabo')                break            num += 1    if breakflag == False:        breakelse:    print('dd')print(divide(rooms))
```

