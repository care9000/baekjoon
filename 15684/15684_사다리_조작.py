import sys
sys.stdin = open('15684_사다리_조작.txt')

def dfs(i, j, cnt):
    global result
    if cnt > result:
        return
    if cnt == result:
        return
    mini_map[i][j] = 1
    mini_map[i][j + 1] = 2
    if check():
        if result > cnt:
            result = cnt

    else:
        for k in range(j + 1, N):
            if mini_map[i][k] == 0 and mini_map[i][k + 1] == 0:
                dfs(i, k, cnt + 1)
        for l in range(i + 1, H + 1):
            for k in range(1, N):
                if mini_map[l][k] == 0 and mini_map[l][k + 1] == 0:
                    dfs(l, k, cnt + 1)
    mini_map[i][j] = 0
    mini_map[i][j + 1] = 0



def check():
    for j in range(1, N + 1):
        if simulation(j):
            continue

        else:
            return False

    return True


def simulation(num):
    start = num
    for i in range(1, H + 1):
        if mini_map[i][num] == 1:
            num += 1

        elif mini_map[i][num] == 2:
            num -= 1

        else:
            continue

    if num == start:
        return True
    return False


N, M, H = map(int, sys.stdin.readline().split())
mini_map = [[0 for _ in range(N + 1)] for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mini_map[a][b] = 1
    mini_map[a][b + 1] = 2

result = 4
if check():
    print(0)
else:
    for i in range(1, H + 1):
        for j in range(1, N):
            if mini_map[i][j] == 0 and mini_map[i][j + 1] == 0:
                dfs(i, j, 1)
    print("-1" if result == 4 else result)