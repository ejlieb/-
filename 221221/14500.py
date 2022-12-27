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
    for m in range(4):
        next_x = sp[0] + nx[m]
        next_y = sp[1] + ny[m]
        if 0 <= next_x < N and 0 <= next_y < M:
            if visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                dfs((next_x, next_y), value + grid[next_x][nhext_y], stage + 1)
                visited[next_x][next_y] = 0
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
