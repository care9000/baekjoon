import sys
sys.stdin = open('17070_파이프_옮기기_1.txt')
import collections

def dfs(i, j):
    global cnt
    q = collections.deque([])
    q.append([i, j, 0])

    while(len(q)):

        i, j, type = q.pop()

        if i == N - 1 and j == N - 1:
            cnt += 1
        if type == 0:
            if type_0(i, j):
                q.append([i, j + 1, 0])
            if type_1(i, j):
                q.append([i + 1, j + 1, 1])
        elif type == 1:
            if type_0(i, j):
                q.append([i, j + 1, 0])
            if type_1(i, j):
                q.append([i + 1, j + 1, 1])
            if type_2(i, j):
                q.append([i + 1, j, 2])

        else:
            if type_2(i, j):
                q.append([i + 1, j, 2])
            if type_1(i, j):
                q.append([i + 1, j + 1, 1])




# 0 가로
def type_0(i, j):
    if -1 < j + 1 < N and mini_map[i][j + 1] == 0:
        return True
    return False

# 1 대각선
def type_1(i, j):
    if type_0(i, j) and type_2(i, j) and mini_map[i + 1][j + 1] == 0:
        return True
    return False
# 2 세로로
def type_2(i, j):
    if -1 < i + 1 < N and mini_map[i + 1][j] == 0:
        return True
    return False
N = int(input())

mini_map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1)
print(cnt)