import sys
sys.stdin = open('17837_새로운_게임.txt')

def simulation():
    global result
    cnt = 1
    while cnt < 1000:
        result = cnt
        for k in range(K):
            i = horse[k][0]
            j = horse[k][1]
            dir = horse[k][2] - 1
            location = horse[k][3]
            move = []
            move.append(k + 1)
            mini_map[i][j][location] = 0
            while location < 3:
                if mini_map[i][j][location + 1] != 0:
                    move.append(mini_map[i][j][location + 1])
                    mini_map[i][j][location + 1] = 0
                else:
                    break

                location += 1

            i_tem = i + dx[dir]
            j_tem = j + dy[dir]
            if ispass(i_tem, j_tem):
                # 흰색일 경우
                if map_info[i_tem][j_tem] == 0:
                    white(i_tem, j_tem, move)
                    if len(move):
                        return

                # 빨간색일 경우
                elif map_info[i_tem][j_tem] == 1:
                    red(i_tem, j_tem, move)
                    if len(move):
                        return

                # 파란색인경우
                else:
                    if dir % 2 == 0:
                        dir += 1
                    else:
                        dir -= 1
                    horse[move[0] - 1][2] = dir + 1
                    #방향반대로 하고 한칸앞이 벽이거나 파란색일 경우
                    if iswall(i + dx[dir], j + dy[dir]) or map_info[i + dx[dir]][j + dy[dir]] == 2:
                        l = 0

                        while l < 4 and len(move):
                            if mini_map[i][j][l] == 0:
                                Hour = move.pop(0)
                                mini_map[i][j][l] = Hour
                            l += 1

                    else:
                        l = 0
                        i_tem = i + dx[dir]
                        j_tem = j + dy[dir]
                        l = 0
                        if map_info[i_tem][j_tem] == 0:
                            white(i_tem, j_tem, move)

                        elif map_info[i_tem][j_tem] == 1:
                            red(i_tem, j_tem, move)

                       if len(move):
                            return

            else:
                if dir % 2 == 0:
                    dir += 1
                else:
                    dir -= 1
                horse[move[0] - 1][2] = dir + 1
                # 방향반대로 하고 한칸앞이 벽이거나 파란색일 경우
                if iswall(i + dx[dir], j + dy[dir]) or map_info[i + dx[dir]][j + dy[dir]] == 2:
                    l = 0
                    while l < 4 and len(move):
                        if mini_map[i][j][l] == 0:
                            Hour = move.pop(0)
                            mini_map[i][j][l] = Hour
                        l += 1

                else:
                    l = 0
                    i_tem = i + dx[dir]
                    j_tem = j + dy[dir]
                    if map_info[i_tem][j_tem] == 0:
                        white(i_tem, j_tem, move)

                    elif map_info[i_tem][j_tem] == 1:
                        red(i_tem, j_tem, move)

                   if len(move):
                        return

            for a in horse:
                if a[3] == 3:
                    return
        cnt += 1
    result = -1
    return


def red(i_tem, j_tem, move):
    l = 0
    while l < 4 and len(move) != 0:
        if mini_map[i_tem][j_tem][l] == 0:
            Hour = move.pop()
            mini_map[i_tem][j_tem][l] = Hour
            horse[Hour - 1][0] = i_tem
            horse[Hour - 1][1] = j_tem
            horse[Hour - 1][3] = l
        l += 1


def white(i_tem, j_tem, move):
    l = 0
    while l < 4 and len(move) != 0:
        if mini_map[i_tem][j_tem][l] == 0:
            Hour = move.pop(0)
            mini_map[i_tem][j_tem][l] = Hour
            horse[Hour - 1][0] = i_tem
            horse[Hour - 1][1] = j_tem
            horse[Hour - 1][3] = l
        l += 1


def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True

    return False


def iswall(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return True
    return False

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]



N, K = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]

horse = [list(map(int, input().split())) for _ in range(K)]


mini_map = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]

for i in range(K):
    mini_map[horse[i][0] - 1][horse[i][1] - 1][0] = i + 1
    horse[i].append(0)
    horse[i][0] -= 1
    horse[i][1] -= 1



result = 1

simulation()
print(result)