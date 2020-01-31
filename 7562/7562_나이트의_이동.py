import sys
sys.stdin = open("7562_나이트의_이동.txt")


import collections
def bfs(i, j, cnt):
    q = collections.deque([])
    q.append([i, j, cnt])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        my_cnt = location[2]
        for k in range(8):
            i_tem = i_location + i_move[k]
            j_tem = j_location + j_move[k]
            if ispass(i_tem, j_tem):
                visited[i_tem][j_tem] = 1
                if i_tem == finish[0] and j_tem == finish[1]:
                    return my_cnt + 1
                q.append([i_tem, j_tem, my_cnt + 1])


def ispass(i, j):
    if -1 < i < I and -1 < j < I and visited[i][j] == 0:
        return True
    return False


i_move = [-2, -2, -1, -1, 1, 1, 2, 2]
j_move = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())
for tc in range(T):
    I = int(input())
    finish = list(map(int, input().split()))
    start = list(map(int, input().split()))

    visited = [[0] * I for _ in range(I)]
    visited[start[0]][start[1]] = 1
    if finish[0] == start[0] and finish[1] == start[1]:
        print(0)
    else:
        print(bfs(start[0], start[1], 0))
