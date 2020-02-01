import sys
sys.stdin = open('2823_유턴_싫어.txt')


def check(i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if ispass(nx, ny):
            cnt += 1
    if cnt == 1:
        return False
    return True

def ispass(i, j):
    if -1 < i < R and -1 < j < C and mini_map[i][j] == '.':
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())

mini_map = [input() for _ in range(R)]

flag = 0
for i in range(R):
    for j in range(C):
        if mini_map[i][j] == '.':
            if check(i, j):
                pass
            else:

                flag = 1

print(flag)