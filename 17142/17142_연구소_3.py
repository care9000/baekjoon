import sys
sys.stdin = open('17142_연구소_3.txt')

import collections
def simlulation():
    global time_min
    tem_map = [[0 for _ in range(N)] for _ in range(N)]
    # 똑 같은 맵 하나 복사 해줌
    cnt = 0
    for i in range(N):
        for j in range(N):
            tem_map[i][j] = mini_map[i][j]
            if tem_map[i][j] == 0:
                cnt += 1
    activated_virus = collections.deque([])
    for i in range(len(A)):
        if A[i] == 1:
            tem_map[viruses[i][0]][viruses[i][1]] = 2
            activated_virus.append([viruses[i][0], viruses[i][1], 0])
        else:
            tem_map[viruses[i][0]][viruses[i][1]] = 9
    time = 0
    if cnt == 0:
        if time < time_min:
            time_min = time

    while len(activated_virus) and cnt > 0:
        # print(activated_virus)
        i, j, time = activated_virus.popleft()
        if time > time_min:
            return
        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if ispass(i_tem, j_tem):
                if tem_map[i_tem][j_tem] == 0:
                    tem_map[i_tem][j_tem] = 2
                    cnt -= 1
                    activated_virus.append([i_tem, j_tem, time + 1])
                elif tem_map[i_tem][j_tem] == 9:
                    tem_map[i_tem][j_tem] = 2
                    activated_virus.append([i_tem, j_tem, time + 1])

    if cnt == 0:
        time += 1
    for i in range(N):
        for j in range(N):
            if tem_map[i][j] == 0:
                return
    if time < time_min:
        time_min = time

def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def PowerSet(n, m, cnt):
    if cnt > M:
        return

    if cnt == M:
        # 활성화 시킬 바이러스만 가지고 simulation ㄱㄱ
        # if A == [1, 1, 1, 0, 0]:
        simlulation()
        return

    elif m == n:

        return
    else:
        A[m] = 1
        PowerSet(n, m + 1, cnt + 1)
        A[m] = 0
        PowerSet(n, m + 1, cnt)





#N 배열의 크기  M 활성화 시킬 바이러스 크기
N, M = map(int, input().split())

mini_map = [list(map(int, input().split())) for _ in range(N)]

viruses = []


for i in range(N):
    for j in range(N):
        if mini_map[i][j] == 2:
            viruses.append([i, j])

# 부분집합 만들어 활성 화 시킬 바이러스를 1 비활성 화 바이러스를 0으로 만들어 줌
A = [0 for _ in range(len(viruses))]
time_min = 987654321
PowerSet(len(viruses), 0, 0)
if time_min == 987654321:
    print(-1)
else:
    print(time_min)


