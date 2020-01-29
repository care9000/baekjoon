import sys
sys.stdin = open('1261_알고스팟.txt')
import collections

def simulation(i, j):
    q = collections.deque([])
    q.append([i, j])
    while len(q):

        i, j = q.popleft()
        if i == N - 1 and j == M - 1:
            return
        cnt = visited[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if is_pass(nx, ny) and visited[nx][ny] == 987654321:
                # 벽 일때
                if int(mini_map[nx][ny]):
                    if is_wall(nx, ny, cnt):
                        q.append([nx, ny])
                # 벽이 아닐때
                else:
                    if is_not_wall(nx, ny, cnt):
                        q.appendleft([nx, ny])


def is_not_wall(i, j, cnt):
    if cnt < visited[i][j]:
        visited[i][j] = cnt
        return True
    return False
def is_wall(i, j, cnt):
    if cnt + 1 < visited[i][j]:
        visited[i][j] = cnt + 1
        return True
    return False

def is_pass(i, j):
    if -1 < i < N and -1 < j < M:
        return True
    return False
dx = [-1, 0, 1, 0,]
dy = [0, -1, 0, 1,]

M, N = map(int, input().split())
mini_map = [sys.stdin.readline() for _ in range(N)]

visited = [[987654321 for _ in range(M)] for _ in range(N)]
visited[0][0] = 0
simulation(0, 0)

print(visited[-1][-1])