import sys
sys.stdin = open('2151_거울_설치.txt')
import collections


def simulation(i, j):
    q = collections.deque([])
    dir = -1
    for k in range(4):
        i_tem = i + dx[k]
        j_tem = j + dy[k]
        if ispass(i_tem, j_tem):
            # 지나갈 수 있으면 appendleft해줄 것
            if mini_map[i_tem][j_tem] == '.':
                q.appendleft([i_tem, j_tem, k, 0])
            # 상하 좌우에 거울을 설치 할 수 있을 경우 설치하거나 설치 안하기(설치하면 append, 설치안하면 leftappend)
            elif mini_map[i_tem][j_tem] == '!':

                q.append([i_tem, j_tem, (k - 1) % 4, 1])
                q.append([i_tem, j_tem, (k + 1) % 4, 1])
                q.appendleft([i_tem, j_tem, k, 0])
            # 바로 도착점 일 경우는 바로 return 해줌
            else:
                return 0

    while len(q):
        i, j, dir, cnt = q.popleft()
        # 이동 가능 한 지 파악(그지점이)
        i_tem = i + dx[dir]
        j_tem = j + dy[dir]
        if ispass(i_tem, j_tem):
            # 그냥 지나가거나 거울을 설치할 수 있음에도 불구하고 설치 안하고 갈 경우
            if mini_map[i_tem][j_tem] == '.' or mini_map[i_tem][j_tem] == '!':
                if cnt < vis[i_tem][j_tem][dir]:
                    vis[i_tem][j_tem][dir] = cnt
                    q.appendleft([i_tem, j_tem, dir, cnt])

            if mini_map[i_tem][j_tem] == '!':
                #왼쪽으로 설치 할 경우
                if cnt + 1 < vis[i_tem][j_tem][(dir + 3) % 4]:
                    vis[i_tem][j_tem][(dir + 3) % 4] = cnt + 1
                    q.append([i_tem, j_tem, (dir + 3) % 4, cnt + 1])
                # 오른쪽으로 설치 할 경우
                if cnt + 1 < vis[i_tem][j_tem][(dir + 1) % 4]:
                    vis[i_tem][j_tem][(dir + 1) % 4] = cnt + 1
                    q.append([i_tem, j_tem, (dir + 1) % 4, cnt + 1])

            # 도착점에 도착하게 되면 더이상 할 필요 없이 리턴
            if i_tem == finish[0] and j_tem == finish[1]:
                vis[finish[0]][finish[1]][dir] = cnt
                return cnt


def ispass(i, j):
    if -1 < i < N and -1 < j < N and mini_map[i][j] != '*':
        return True
    return False


# 4방향(북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
mini_map = list(input() for _ in range(N))
start = []
finish = []
flag = 0

for i in range(N):
    for j in range(N):
        if mini_map[i][j] == '#':
            if flag == 0:
                start.append(i)
                start.append(j)
                flag = 1

            else:
                finish.append(i)
                finish.append(j)

vis = [[[987654321 for _ in range(4)]for _ in range(N)]for _ in range(N)]

print(simulation(start[0], start[1]))
