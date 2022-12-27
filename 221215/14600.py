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