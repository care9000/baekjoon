import sys
sys.stdin = open('16137_견우와_직녀.txt')

import collections


def bfs(i, j, cnt):
    q = collections.deque([])
    visited_cnt_1[i][j] = 1
    q.append([i, j, cnt, 0, 0])
    while len(q):
        i, j, cnt, time, go = q.popleft()
        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if ispass(i_tem, j_tem):
            # 기회가 1번인 경우와 0 번인 경우를 나눠서 생각.
                if cnt:
                    # 땅인 경우에는 그냥 지나감
                    if mini_map[i_tem][j_tem] == 1:
                        if visited_cnt_1[i_tem][j_tem] > time + 1:
                            visited_cnt_1[i_tem][j_tem] = time + 1
                            q.append([i_tem, j_tem, 1, time + 1, 0])
                     # 절벽이고 오작교 설치 가능한 경우
                    elif mini_map[i_tem][j_tem] == 0 and go == 0:
                        test = M
                        zz = 2
                        while test < time + 1:
                            test = M * zz
                            zz += 1
                        if visited_cnt_0[i_tem][j_tem] > test:
                            visited_cnt_0[i_tem][j_tem] = test
                            q.append([i_tem, j_tem, 0, test, 1])

                    elif mini_map[i_tem][j_tem] != -1 and go == 0:
                        test = mini_map[i_tem][j_tem]
                        zz = 2
                        while test < time + 1:
                            test = zz * mini_map[i_tem][j_tem]
                            zz += 1
                        if visited_cnt_1[i_tem][j_tem] > test:
                            visited_cnt_1[i_tem][j_tem] = test
                            q.append([i_tem, j_tem, 1, test, 1])

                else:
                    #그냥 길을 가는 경우
                    if mini_map[i_tem][j_tem] == 1:
                        if visited_cnt_0[i_tem][j_tem] > time + 1:
                            visited_cnt_0[i_tem][j_tem] = time + 1
                            q.append([i_tem, j_tem, 0, time + 1, 0])
                    #오작교 가는경우
                    elif mini_map[i_tem][j_tem] > 1 and go == 0:
                        test = mini_map[i_tem][j_tem]
                        zz = 2
                        while test < time + 1:
                            test = zz * mini_map[i_tem][j_tem]
                            zz += 1

                        if visited_cnt_0[i_tem][j_tem] > test:
                            visited_cnt_0[i_tem][j_tem] = test
                            q.append([i_tem, j_tem, 0, test, 1])








def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True
    return False
# # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# N(배열의크기), M(오작교의 주기)
N, M = map(int, input().split())

mini_map = [list(map(int, input().split())) for _ in range(N)]

# 놀 수 있는 다리 미리 정하기
for i in range(N):
    for j in range(N):
        if mini_map[i][j] == 0:
            around = [0 for _ in range(4)]
            cnt = 0
            for k in range(4):
                i_tem = i + dx[k]
                j_tem = j + dy[k]
                if ispass(i_tem, j_tem) and mini_map[i_tem][j_tem] == 0:
                    cnt += 1
                    around[k] = 1

            if cnt >= 3 or around == [1, 1, 0, 0] or around == [0, 1, 1, 0] or around == [0, 0, 1, 1]  or around == [1, 0, 0, 1]:
                mini_map[i][j] = -1


visited_cnt_0 = [[9876543210 for _ in range(N)] for _ in range(N)]
visited_cnt_1 = [[9876543210 for _ in range(N)] for _ in range(N)]
bfs(0, 0, 1)
print(min(visited_cnt_1[-1][-1], visited_cnt_0[-1][-1]))

