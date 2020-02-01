import sys
sys.stdin = open('17135_캐슬_디펜스.txt')

import collections
def simulation():
    global result
    tem_mini_map = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if mini_map[i][j] == 1:
                tem_mini_map[i][j] = 1

    tem_hunt = 0
    while 1:
        hunts = []
        # print(A)
        # print(tem_mini_map)
        for i in range(M):
            if A[i]:
                find_hunt(i, tem_mini_map, hunts)

        # print(hunts)
        for hunt in hunts:
            if tem_mini_map[hunt[0]][hunt[1]] == 1:
                tem_hunt += 1
                tem_mini_map[hunt[0]][hunt[1]] = 0
        # print(tem_hunt)
        if tem_hunt > result:
            result = tem_hunt




        for i in range(N - 1, -1, -1):
            for j in range(M):
                tem_mini_map[i][j] = tem_mini_map[i - 1][j]
        for j in range(M):
            tem_mini_map[0][j] = 0

        flag = 0
        for i in range(N):
            for j in range(M):
                if tem_mini_map[i][j] == 1:
                    flag = 1
                    break
        if flag == 0:
            return

def find_hunt(location, tem_mini_map, hunts):
    tems = []
    if tem_mini_map[N - 1][location] == 1:
        hunts.append([N - 1, location])
        return
    else:
        q = collections.deque([])
        q.append([N - 1, location, 1])
        vis = [[0 for _ in range(M)] for _ in range(N)]
        while len(q):
            i, j, cnt = q.popleft()
            if cnt < D:
                for k in range(3):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if ispass(nx, ny) and vis[nx][ny] == 0:
                        if tem_mini_map[nx][ny] == 1:
                            vis[nx][ny] = 1
                            tems.append([nx, ny, cnt + 1])
                        else:
                            vis[nx][ny] = 1
                            q.append([nx, ny, cnt + 1])
        tem_result = 987654321
        tem_i = -1
        tem_j = -1
        for tem in tems:
            if tem_result > tem[2]:
                tem_i = tem[0]
                tem_j = tem[1]
                tem_result = tem[2]
            elif tem_result == tem[2] and tem_j > tem[1]:
                tem_i = tem[0]
                tem_j = tem[1]
        if tem_i != -1 and tem_j != -1:
            hunts.append([tem_i, tem_j])
        return


def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        return True

    return False


def PowerSet(n, m, cnt):
    if n == m:
        if cnt == 3:
            # if A == [0, 1, 1, 1, 0]:
            simulation()

    elif cnt > 3:
        return

    else:
        A[m] = 1
        PowerSet(n, m + 1, cnt + 1)
        A[m] = 0
        PowerSet(n, m + 1, cnt)


dx = [-1, 0, 0]
dy = [0, 1, -1]

result = 0
N, M, D = map(int, sys.stdin.readline().split())
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = [0 for _ in range(M)]
PowerSet(M, 0, 0)
print(result)