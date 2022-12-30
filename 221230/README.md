# 백준 #11049

https://www.acmicpc.net/problem/11049

DP

이차원 배열 `DP[i][j]`는 i~j번까지 행렬의 최소 연산 수를 저장한다. `DP[i][i]`는 0을 저장하고 있다. 2개의 행렬의 합인 차이 1의  `DP[i][i+1]`은 주어진 식대로 행렬의 연산 횟수를 구한다. 





```python
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N): 
    for j in range(0, N - i):

        if i == 1:
            dp[j][j + i] = matrix[j][0] * matrix[j][1] * matrix[j + i][1]
            continue

        dp[j][j + i] = 2 ** 32
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i],
                               dp[j][k] + dp[k + 1][j + i] + matrix[j][0] * matrix[k][1] * matrix[j + i][1])

print(dp[0][N - 1])
```

