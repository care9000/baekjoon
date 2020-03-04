import sys
sys.stdin = open('1726_로봇.txt')
import collections
def bfs():
    q = collections.deque([])
    # i좌표, j좌표, dir, cnt 담아줌
    q.append([start[0] - 1, start[1] - 1, start[2], 0])
    vis[start[0] - 1][start[1] - 1][start[2]] = 0
    while len(q):
        i, j, dir, cnt = q.popleft()
        if i == finish[0] - 1 and j == finish[1] - 1 and dir == finish[2]:
            return cnt
        # 명령 1 go k
        for move in range(1, 4):
            i_tem = i + (move * dx[dir])
            j_tem = j + (move * dy[dir])
            if ispass(i_tem, j_tem):
                if vis[i_tem][j_tem][dir] > cnt + 1:
                    vis[i_tem][j_tem][dir] = cnt + 1
                    q.append([i_tem, j_tem, dir, cnt + 1])
            else:
                break

        # 명령 turn dir
        if dir > 2:
            for dir_tem in range(1, 3):
                if vis[i][j][dir_tem] > cnt + 1:
                    vis[i][j][dir_tem] = cnt + 1
                    q.append([i, j, dir_tem, cnt + 1])

        else:
            for dir_tem in range(3, 5):
                if vis[i][j][dir_tem] > cnt + 1:
                    vis[i][j][dir_tem] = cnt + 1
                    q.append([i, j, dir_tem, cnt + 1])


def ispass(i, j):
    if -1 < i < M and -1 < j < N and mini_map[i][j] == 0:
        return True

    return False


# 방향(X 동 서 남 북)
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

M, N = map(int, input().split())
mini_map = [list(map(int, input().split())) for _ in range(M)]
start = list(map(int, input().split()))
finish = list(map(int, input().split()))

vis = [[[987654321 for _ in range(5)] for _ in range(N)] for _ in range(M)]

print(bfs())
