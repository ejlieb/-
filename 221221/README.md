# 백준 #14500

https://www.acmicpc.net/problem/14500

DFS를 사용하여 풀이할 수 있다. 테트로미노 모양 중 중앙에서 한칸 뻗어나가는 ㅗ 모양 외에 모든 모양은 한 점을 기준으로 3칸 더 진행한 DFS로 판별 가능하다. 따라서 DFS로 나머지 모든 모양을 체크한 뒤 ㅗ 모양을 판별하는 함수 middle을 함께 실행시켜 최대값을 구한다.

middle함수의 경우 각 시작점에서 상하좌우를 체크하고(격자 밖인지), 갈 수 있는 곳이면 value를 더하고 몇개를 갈 수 있나 체크한다. 만약 4개이면( 총 5개 십자가 모양) 그 중 시작점을 제외한 최솟값을 빼줘 최대값을 구하고 3개이면(총 4 개 ㅗ 모양) 그대로 value를 구한다. 그 중 최대값을 판별한다.

```python
import sys
input = sys.stdin.readline
N, M = list(map(int,(input().split())))
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_val = 0
m_v = max(map(max, grid))

def dfs(sp, value, stage):
    global grid, visited, max_val
    if value + m_v * (4 - stage) <= max_val:
        return
    if stage == 4:
        if value > max_val:
            max_val = value
        return
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    # visited[sp[0]][sp[1]] = 1
    for m in range(4):
        next_x = sp[0] + nx[m]
        next_y = sp[1] + ny[m]
        if 0 <= next_x < N and 0 <= next_y < M:
            if visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                dfs((next_x, next_y), value + grid[next_x][next_y], stage + 1)
                visited[next_x][next_y] = 0
    # visited[sp[0]][sp[1]] = 0
    return


def middle(sp):
    global grid, max_val
    min_val = 1e10
    value = grid[sp[0]][sp[1]]
    flag = 0
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    for m in range(4):
        next_x = sp[0] + nx[m]
        next_y = sp[1] + ny[m]
        if 0 <= next_x < N and 0 <= next_y < M:
            flag += 1
            value += grid[next_x][next_y]
            if grid[next_x][next_y] < min_val:
                min_val = grid[next_x][next_y]
    if flag == 3:
        if value >= max_val:
            max_val = value
    elif flag == 4:
        value -= min_val
        if value >= max_val:
            max_val = value



for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs((i, j), grid[i][j], 1)
        middle((i,j))
        visited[i][j] = 0


print(max_val)
```

