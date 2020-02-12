import sys
sys.stdin = open('14890_경사로.txt')

def horizontal_simulaion(i):
    global result
    j = 1
    vis = [0 for _ in range(N)]
    while j < N:

        # 이전보다 오르막일 경우
        if mini_map[i][j] == mini_map[i][j - 1] + 1:
            if is_up(i, j - 1, vis):
                for k in range(1, L + 1):
                    vis[j - k] = 1

                j += 1
            else:
                return

        #이전이랑 같을 경우
        elif mini_map[i][j] == mini_map[i][j - 1]:
            j += 1

        #이전보다 내리막 일경우
        elif mini_map[i][j] + 1 == mini_map[i][j - 1]:
            if is_down(i, j, vis):
                for k in range(L):
                    vis[j + k] = 1
                j += L
            else:
                return

        else:
            return

    result += 1


def vertical_simulation(i):
    global result
    j = 1
    vis = [0 for _ in range(N)]
    while j < N:

        # 이전보다 오르막일 경우
        if mini_map[j][i] == mini_map[j - 1][i] + 1:
            if is_up2(i, j - 1, vis):
                for k in range(1, L + 1):
                    vis[j - k] = 1

                j += 1
            else:
                return

        #이전이랑 같을 경우
        elif mini_map[j][i] == mini_map[j - 1][i]:
            j += 1

        #이전보다 내리막 일경우
        elif mini_map[j][i] + 1 == mini_map[j - 1][i]:
            if is_down2(i, j,vis):
                for k in range(L):
                    vis[j + k] = 1
                j += L
            else:
                return

        else:
            return

    result += 1




def is_down(i, j, vis):
    for k in range(1, L):
        # L만큼 경사로의 길이가 값들과 같아야 경사로를 설치 할 수 있음.
        if j + k < N and mini_map[i][j] == mini_map[i][j + k] and vis[j + k] == 0:
            pass
        else:
            return False
    # 그다음 것은 그경사로보다 값이 크면 안됨.
    if j + L == N or mini_map[i][j + L] <= mini_map[i][j]:
        return True
    return False


def is_down2(i, j, vis):
    for k in range(1, L):
        if j + k < N and mini_map[j][i] == mini_map[j + k][i] and vis[j + k] == 0:
            pass
        else:
            return False

    if j + L == N or mini_map[j + L][i] <= mini_map[j][i]:
        return True
    return False


def is_up(i, j, vis):
    # L만큼 경사로의 길이가 값들과 같아야 경사로를 설치 할 수 있음.
    for k in range(1, L):
        if j - k > -1 and mini_map[i][j] == mini_map[i][j - k] and vis[j - k] == 0:
            pass
        else:
            return False
    # 그다음 것은 그경사로보다 값이 작으면 안됨.
    if j - L < 0 or mini_map[i][j - L] <= mini_map[i][j]:
        return True
    return False


def is_up2(i, j, vis):
    for k in range(1, L):
        if j - k > -1 and mini_map[j][i] == mini_map[j - k][i] and vis[j - k] == 0:
            pass
        else:
            return False

    if j - L < 0 or mini_map[j - L][i] <= mini_map[j][i]:
        return True
    return False


N, L = map(int, input().split())
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


result = 0
for i in range(N):
    horizontal_simulaion(i)
    vertical_simulation(i)

print(result)

