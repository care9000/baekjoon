import sys
sys.stdin = open('2.txt')
import collections

def bfs(i, j):
    # 맨처음 코드 초기화
    q = collections.deque([])
    q.append([i, j, my_code[:], 0])

    while len(q):
        i, j, code, cnt = q.popleft()
        # 도착했으므로 return 시킴
        if i == N - 1 and j == N - 1:
            return cnt
        # 4방향 탐색
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if -1 < nx < N and -1 < ny < N:
                # 만약 100보다 크면 할 필요가 없다.
                if cnt < 100:
                    #코드 받기
                    tem = code[1:]
                    tem.append(mini_map[nx][ny])
                    if is_code1(tem):
                        tem = [-1, -1, -1, mini_map[0][0]]
                        if is_go_code1(tem):
                            visited[0][0].append(tem[:])
                            q.append([0, 0, tem, cnt + 1])

                    elif is_code2(tem):
                        tem = [-1, -1, -1, mini_map[(N // 2) - 1][(N // 2) - 1]]

                        if is_go_code2(tem):
                            visited[(N // 2)][(N // 2)].append(tem[:])
                            q.append([(N // 2) - 1, (N // 2) - 1, tem, cnt + 1])

                    elif is_code3(tem):
                        for k in range(4):
                            nx = i + dx[k]
                            ny = j + dy[k]
                            if -1 < nx < N and -1 < ny < N:
                                tem = [-1, -1, -1, -1]
                                visited[nx][ny].append(tem[:])
                                q.appendleft([nx, ny, tem, cnt])

                    else:
                        tem = code[1:]
                        tem.append(mini_map[nx][ny])
                        if tem not in visited[nx][ny]:
                            visited[nx][ny].append(tem[:])
                            q.append([nx, ny, tem, cnt + 1])
    return -1


def is_code1(list):
    if list in code_a:
        return True
    return False


def is_go_code1(list):
    if list not in visited[0][0]:
        return True
    return False


def is_code2(list):
    if list in code_b:
        return True
    return False


def is_go_code2(list):
    if list not in visited[N // 2][N // 2]:
        return True
    return False


def is_code3(list):
    if list in code_c:
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mini_map = [list(map(int, input().split())) for _ in range(N)]
    dummy = list(map(int, input().split()))
    code_a = [list(map(int, input().split())) for _ in range(dummy[0])]
    code_b = [list(map(int, input().split())) for _ in range(dummy[1])]
    code_c = [list(map(int, input().split())) for _ in range(dummy[2])]

    #코드 초기화
    my_code = list()
    for i in range(4):
        my_code.append(-1)

    # 배열을 3차원으로 받음
    visited = [[[] for _ in range(N)] for _ in range(N)]


    print("#{} {}".format(tc, bfs(0, 0)))
