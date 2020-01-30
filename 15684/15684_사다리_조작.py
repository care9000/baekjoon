import sys
sys.stdin = open('15684_사다리_조작.txt')

def chance_1():
    for i in range(1, H + 1):
        for j in range(1, N):
            if mini_map[i][j] == 0 and mini_map[i][j + 1] != 1:
                mini_map[i][j] = 1
                mini_map[i][j + 1] = 2
                if check():
                    return True

                mini_map[i][j] = 0
                mini_map[i][j + 1] = 0

def chance_2():
    for i in range(1, H + 1):
        for j in range(1, N):
            if mini_map[i][j] == 0 and mini_map[i][j + 1] != 1:
                mini_map[i][j] = 1
                mini_map[i][j + 1] = 2

                for k in range(i, H + 1):
                    if k == i:
                        for l in range(j + 1, N):
                            if mini_map[k][l] == 0 and mini_map[k][l + 1] != 1:
                                mini_map[k][l] = 1
                                mini_map[k][l + 1] = 2
                                if check():
                                    return True
                                mini_map[k][l] = mini_map[k][l + 1] = 0

                    else:
                        for l in range(1, N):
                            if mini_map[k][l] == 0 and mini_map[k][l + 1] != 1:
                                mini_map[k][l] = 1
                                mini_map[k][l + 1] = 2
                                if check():
                                    return True
                                mini_map[k][l] = mini_map[k][l + 1] = 0

                mini_map[i][j] = mini_map[i][j + 1] = 0

def chance_3():
    for i in range(1, H + 1):
        for j in range(1, N):
            if mini_map[i][j] == 0 and mini_map[i][j + 1] != 1:

                mini_map[i][j] = 1
                mini_map[i][j + 1] = 2

                for k in range(i, H + 1):
                    if k == i:
                        for l in range(j + 1, N):
                            if mini_map[k][l] == 0 and mini_map[k][l + 1] != 1:
                                mini_map[k][l] = 1
                                mini_map[k][l + 1] = 2
                                for m in range(k, H + 1):
                                    if m == k:
                                        for n in range(k + 1, N):
                                            if mini_map[m][n] == 0 and mini_map[m][n + 1] != 1:
                                                mini_map[m][n] = 1
                                                mini_map[m][n + 1] = 2
                                                if check():
                                                    return True
                                                mini_map[m][n + 1] = mini_map[m][n] = 0
                                    else:
                                        for n in range(1, N):
                                            if mini_map[m][n] == 0 and mini_map[m][n + 1] != 1:
                                                mini_map[m][n] = 1
                                                mini_map[m][n + 1] = 2
                                                if check():
                                                    return True
                                                mini_map[m][n + 1] = mini_map[m][n] = 0
                                mini_map[k][l] = mini_map[k][l + 1] = 0

                    else:
                        for l in range(1, N):

                            if mini_map[k][l] == 0 and mini_map[k][l + 1] != 1:
                                mini_map[k][l] = 1
                                mini_map[k][l + 1] = 2
                                for m in range(k, H + 1):
                                    if m == k:
                                        for n in range(l + 1, N):
                                            if mini_map[m][n] == 0 and mini_map[m][n + 1] != 1:
                                                mini_map[m][n] = 1
                                                mini_map[m][n + 1] = 2
                                                if check():
                                                    return True
                                                mini_map[m][n + 1] = mini_map[m][n] = 0
                                    else:
                                        for n in range(1, N):
                                            if mini_map[m][n] == 0 and mini_map[m][n + 1] != 1:
                                                mini_map[m][n] = 1
                                                mini_map[m][n + 1] = 2
                                                if check():
                                                    return True
                                                mini_map[m][n + 1] = mini_map[m][n] = 0
                                mini_map[k][l] = mini_map[k][l + 1] = 0

                mini_map[i][j] = mini_map[i][j + 1] = 0





def check():
    for j in range(1, N + 1):
        if simulation(j):
            continue
        else:
            return False
    return True

def simulation(num):
    start = num

    for i in range(1, H + 1):
        if mini_map[i][num] == 1:
            num += 1

        elif mini_map[i][num] == 2:
            num -= 1
        else:
            continue



    if num == start:
        return True
    return False


N, M, H = map(int, sys.stdin.readline().split())

mini_map = [[0 for _ in range(N + 1)] for _ in range(H + 1)]


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mini_map[a][b] = 1
    mini_map[a][b + 1] = 2

# mini_map[4][1] = mini_map[3][2] = mini_map[4][3] = 1
# mini_map[4][2] = mini_map[3][3] = mini_map[4][4] = 2
#


if check():
    print(0)
elif chance_1():
    print(1)
elif chance_2():
    print(2)
elif chance_3():
    print(3)
else:
    print(-1)