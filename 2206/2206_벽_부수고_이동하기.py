import sys
sys.stdin = open('2206_벽_부수고_이동하기.txt')

import collections
def bfs(i, j):
    q = collections.deque([])
    q.append([i, j, 1, 1])
    visited_cnt_1[i][j] = 1
    visited_cnt_0[i][j] = 1
    while len(q):
        i, j, cnt, reach = q.popleft()
        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if -1 < i_tem < N and -1 < j_tem < M:
                #cnt 가 1 일때 와 0 일때 구분
                if cnt:
                    # 벽이 아닐 경우
                    if mini_map[i_tem][j_tem] == 0:
                        if visited_cnt_1[i_tem][j_tem] > reach + 1:
                            visited_cnt_1[i_tem][j_tem] = reach + 1
                            q.append([i_tem, j_tem, 1, reach + 1])
                        if visited_cnt_0[i_tem][j_tem] > reach + 1:
                            visited_cnt_0[i_tem][j_tem] = reach + 1

                    # 벽 일 경우
                    else:
                        if visited_cnt_0[i_tem][j_tem] > reach + 1:
                            visited_cnt_0[i_tem][j_tem] = reach + 1
                            q.append([i_tem, j_tem, 0, reach + 1])

                # cnt 가 0 일 경우
                else:
                    if mini_map[i_tem][j_tem] == 0:
                        if visited_cnt_0[i_tem][j_tem] > reach + 1:
                            visited_cnt_0[i_tem][j_tem] = reach + 1
                            q.append([i_tem, j_tem, 0, reach + 1])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

dummy = list(input() for _ in range(N))
mini_map = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        mini_map[i][j] = int(dummy[i][j])



visited_cnt_1 = [[987654321 for _ in range(M)] for _ in range(N)]

visited_cnt_0 = [[987654321 for _ in range(M)] for _ in range(N)]


bfs(0, 0)
result = min(visited_cnt_0[-1][-1], visited_cnt_1[-1][-1])
if result != 987654321:
    print(result)
else:
    print(-1)