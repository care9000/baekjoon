import sys
sys.stdin = open('15683_감시.txt')


def dfs_0(i, j):
    visited[i][j] = 1
    i_tem = i
    j_tem = j - 1
    if -1 < i_tem < N and -1 < j_tem < M and my_map[i_tem][j_tem] != 6:
        dfs_0(i_tem, j_tem)

def dfs_1(i, j):
    visited[i][j] = 1
    i_tem = i + 1
    j_tem = j
    if -1 < i_tem < N and -1 < j_tem < M and my_map[i_tem][j_tem] != 6:
        dfs_1(i_tem, j_tem)

def dfs_2(i, j):
    visited[i][j] = 1
    i_tem = i
    j_tem = j + 1
    if -1 < i_tem < N and -1 < j_tem < M and my_map[i_tem][j_tem] != 6:
        dfs_2(i_tem, j_tem)

def dfs_3(i, j):
    visited[i][j] = 1
    i_tem = i - 1
    j_tem = j
    if -1 < i_tem < N and -1 < j_tem < M and my_map[i_tem][j_tem] != 6:
        dfs_3(i_tem, j_tem)


def Perm(my_max, m):
    global area
    if my_max == m:
        for i in range(N):
            for j in range(M):
                visited[i][j] = 0

        # 탐색 시작
        for z in range(len(direct)):
            if cctv_list[z] == 1:
                if direct[z] == 0:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 1:
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 2:
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                else:
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])

            elif cctv_list[z] == 2:
                if direct[z] == 0:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                else:
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])

            elif cctv_list[z] == 3:
                if direct[z] == 0:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 1:
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 2:
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
                else:
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])

            elif cctv_list[z] == 4:
                if direct[z] == 0:
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 1:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
                elif direct[z] == 2:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
                else:
                    dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                    dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
            else:
                dfs_0(cctv_location_list[z][0], cctv_location_list[z][1])
                dfs_1(cctv_location_list[z][0], cctv_location_list[z][1])
                dfs_2(cctv_location_list[z][0], cctv_location_list[z][1])
                dfs_3(cctv_location_list[z][0], cctv_location_list[z][1])
        cnt = 0
        for ii in range(N):
            for jj in range(M):

                if visited[ii][jj] == 0 and my_map[ii][jj] != 6:
                    cnt += 1
                    if cnt > area:
                        return

        if area > cnt:
            area = cnt




    else:
        # 두번째는 2번 탐색
        if cctv_list[m] == 2:
            for a in range(2):
                direct[m] = a
                Perm(my_max, m + 1)

        # 다섯번째는 1번 탐색
        elif cctv_list[m] == 5:
            direct[m] = 0
            Perm(my_max, m + 1)

        else:
            for b in range(4):
                direct[m] = b
                Perm(my_max, m + 1)



N, M = map(int, input().split())

my_map = [list(map(int, input().split())) for _ in range(N)]


cctv_list = []
cctv_location_list = []
for i in range(N):
    for j in range(M):
        if my_map[i][j] and my_map[i][j] != 6:
            cctv_list.append(my_map[i][j])
            cctv_location_list.append([i, j])


direct = [0] * len(cctv_list)
visited = [[0 for _ in range(M)] for _ in range(N)]

# direct = 0 일 때 왼쪽, 1 = 아래 2 오른 3 위
# ex) cctv = 1 일경우 아래만 확인
# ex) cctv = 4 일경우 아래만 못봄
area = 987654321
Perm(len(cctv_list), 0)

print(area)
