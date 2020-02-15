import sys
sys.stdin = open('17143_낚시왕.txt')


def simulation():
    catch = 0
    location = 0
    while location < C:
        location += 1
        # 잡은 상어의 크기를 추가해 주자
        catch += catch_simulation(location)
        # 상어 이동 시키자
        move_simulation()
    return catch


def catch_simulation(location):
    catch = 0
    for i in range(1, R + 1):
        if mini_map[i][location][2]:
            catch += mini_map[i][location][2]
            mini_map[i][location] = [0, 0, 0]
            return catch

    return 0

def move_simulation():
    sharks = []
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if mini_map[i][j] != [0, 0, 0]:
                i_tem = i
                j_tem = j
                dir = mini_map[i][j][1]
                speed = mini_map[i][j][0]
                size = mini_map[i][j][2]
                mini_map[i][j] = [0, 0, 0]
                if dir == 1 or dir == 2:
                    for _ in range(speed % ((R - 1) * 2)):
                        nx = i_tem + dx[dir]
                        ny = j_tem + dy[dir]
                        if ispass(nx, ny):
                            i_tem = nx
                            j_tem = ny

                        else:
                            if dir == 1:
                                dir = 2
                                i_tem += dx[dir]
                                j_tem += dy[dir]

                            else:
                                dir = 1
                                i_tem += dx[dir]
                                j_tem += dy[dir]

                else:
                    for _ in range(speed % ((C - 1) * 2)):
                        nx = i_tem + dx[dir]
                        ny = j_tem + dy[dir]
                        if ispass(nx, ny):
                            i_tem = nx
                            j_tem = ny

                        else:
                            if dir == 3:
                                dir = 4

                            else:
                                dir = 3
                            i_tem += dx[dir]
                            j_tem += dy[dir]
                sharks.append([i_tem, j_tem, speed, dir, size])

    # 그자리에 자신보다 큰 상어가 있으면 그상어는 죽음 ㅠㅠ 죽고 더큰 상어로 대처됨
    for shark in sharks:
        if mini_map[shark[0]][shark[1]] == [0, 0, 0]:
            mini_map[shark[0]][shark[1]] = [shark[2], shark[3], shark[4]]

        elif mini_map[shark[0]][shark[1]][2] < shark[4]:
            mini_map[shark[0]][shark[1]] = [shark[2], shark[3], shark[4]]

def ispass(i, j):
    if 0 < i < R + 1 and 0 < j < C + 1:
        return True

    return False


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())

mini_map = [[[0 for _ in range(3)] for _ in range(C + 1)] for _ in range(R + 1)]
shark_info = [list(map(int, input().split())) for _ in range(M)]

for shark in shark_info:
    mini_map[shark[0]][shark[1]] = [shark[2], shark[3], shark[4]]

print(simulation())