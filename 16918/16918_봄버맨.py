import sys
sys.stdin = open('16918_봄버맨.txt')


def simulation_odd():
    for i in range(R):
        for j in range(C):
            mini_map[i][j] += 1



def simulaion_even():
    booms = []
    for i in range(R):
        for j in range(C):
            if mini_map[i][j] > -1:
                mini_map[i][j] += 1
                if mini_map[i][j] == 4:
                    booms.append([i, j])
    for boom in booms:
        boom_simulatuin(boom[0], boom[1])
        mini_map[boom[0]][boom[1]] = 0


def boom_simulatuin(i, j):
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if -1 < nx < R and -1 < ny < C:
            mini_map[nx][ny] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C, N = map(int, input().split())

dummy = list(input() for _ in range(R))

mini_map = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if dummy[i][j] == 'O':
            mini_map[i][j] = 2

if N > 5:
    N %= 4
    if N < 4:
        N += 4


for time in range(3, N + 2):
    if time % 2 == 0:
        simulaion_even()

    else:
        simulation_odd()

for i in range(R):
    for j in range(C):
        if mini_map[i][j] == 0:
            print('.', end="")
        else:
            print('O', end="")
    print()