import sys
sys.stdin = open('11048_이동하기.txt')



N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = data[0][0]

for i in range(N):
    if i == 0:
        for j in range(1, M):
            dp[i][j] = dp[0][j - 1] + data[i][j]

    else:
        for j in range(M):
            if j == 0:
                dp[i][0] = dp[i - 1][0] + data[i][0]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + data[i][j]

print(dp[-1][-1])
