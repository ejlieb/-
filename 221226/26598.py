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
    print('dd')





