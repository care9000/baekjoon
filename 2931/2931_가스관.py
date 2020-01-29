import sys
sys.stdin = open('2931_가스관.txt')

# 잃어버린 가스 위치 찾기
def find_lostpipe():
    global i_find, j_find
    for gas_pipe in gas_pipes:
        if gas_pipe[2] == 1:
            for k in range(2):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return

        if gas_pipe[2] == 2:
            for k in range(1, 3):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return
        if gas_pipe[2] == 3:
            for k in range(2, 4):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return
        if gas_pipe[2] == 4:
            for k in range(-1, 1, 1):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return
        if gas_pipe[2] == 5:
            for k in range(1, 5, 2):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return
        if gas_pipe[2] == 6:
            for k in range(0, 4, 2):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return
        if gas_pipe[2] == 7:
            for k in range(4):
                x_tem = gas_pipe[0] + dx[k]
                y_tem = gas_pipe[1] + dy[k]
                if mini_map[x_tem][y_tem] == 0:
                    i_find, j_find = x_tem, y_tem
                    return

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]








R, C = map(int, input().split())
dummy = [input() for _ in range(R)]

mini_map = [[0 for _ in range(C)] for _ in range(R)]

gas_pipes = []
i_start = 0
j_start = 0
i_finish = 0
j_finish = 0
# 미니맵에 표시하기
# 5(-) 6(|) 7(+)
for i in range(R):
    for j in range(C):
        if dummy[i][j] == '1':
            mini_map[i][j] = 1
            gas_pipes.append([i, j, 1])
        elif dummy[i][j] == '2':
            mini_map[i][j] = 2
            gas_pipes.append([i, j, 2])
        elif dummy[i][j] == '3':
            mini_map[i][j] = 3
            gas_pipes.append([i, j, 3])
        elif dummy[i][j] == '4':
            mini_map[i][j] = 4
            gas_pipes.append([i, j, 4])
        elif dummy[i][j] == '-':
            mini_map[i][j] = 5
            gas_pipes.append([i, j, 5])
        elif dummy[i][j] == '|':
            mini_map[i][j] = 6
            gas_pipes.append([i, j, 6])
        elif dummy[i][j] == '+':
            mini_map[i][j] = 7
            gas_pipes.append([i, j, 7])
        elif dummy[i][j] == 'M':
            mini_map[i][j] = 8
            i_start = i
            j_start = j
        elif dummy[i][j] == 'Z':
            mini_map[i][j] = 9
            i_finish = 0
            j_finish = 0
i_find = 0
j_find = 0
find_lostpipe()
around = [0 for _ in range(4)]
#잃어버린 가스에서 4방향 위치 확인
# 하 우 상 좌

for k in range(4):
    i_tem = i_find + dx[k]
    j_tem = j_find + dy[k]
    if -1 < i_tem < R and -1 < j_tem < C:
        if mini_map[i_tem][j_tem] == 8:
            around[k] = 8
        elif mini_map[i_tem][j_tem] == 9:
            around[k] = 9
        elif mini_map[i_tem][j_tem] == 7:
            around[k] = 1
        else:
            if k == 0:
                if mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 6:
                    around[k] = 1
            if k == 1:
                if mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 5:
                    around[k] = 1
            if k == 2:
                if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 6:
                    around[k] = 1
            elif k == 3:
                if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 5:
                    around[k] = 1


if around == [1, 1, 0, 0]:
    print(i_find + 1, j_find + 1, 1)
elif around == [0, 1, 1, 0]:
    print(i_find + 1, j_find + 1, 2)
elif around == [0, 0, 1, 1]:
    print(i_find + 1, j_find + 1, 3)
elif around == [1, 0, 0, 1]:
    print(i_find + 1, j_find + 1, 4)
elif around == [1, 0, 1, 0]:
    print(i_find + 1, j_find + 1, '|')
elif around == [0, 1, 0, 1]:
    print(i_find + 1, j_find + 1, '-')
elif around == [1, 1, 1, 1]:
    print(i_find + 1, j_find + 1, '+')
else:
    for i in range(4):
        if around[i] == 8:
            for k in range(4):
                i_tem = i_start + dx[k]
                j_tem = j_start + dy[k]
                if -1 < i_tem < R and -1 < j_tem < C:
                    if mini_map[i_tem][j_tem] == 7:
                        around[i] = 0
                        break
                    elif mini_map[i_tem][j_tem] == 8:
                        around[i] = 0
                        break
                    elif mini_map[i_tem][j_tem] == 9:
                        around[i] = 0
                        break
                    else:
                        if k == 0:
                            if mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 6:
                                around[i] = 0
                                break
                        if k == 1:
                            if mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 5:
                                around[i] = 0
                                break
                        if k == 2:
                            if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 6:
                                around[i] = 0
                                break
                        elif k == 3:
                            if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 5:
                                around[i] = 0
                                break
        if around[i] == 8:
            around[i] = 1
        if around[i] == 9:
            for k in range(4):
                i_tem = i_start + dx[k]
                j_tem = j_start + dy[k]
                if -1 < i_tem < R and -1 < j_tem < C:
                    if mini_map[i_tem][j_tem] == 7:
                        around[i] = 0
                        break
                    elif mini_map[i_tem][j_tem] == 8:
                        around[i] = 0
                        break
                    elif mini_map[i_tem][j_tem] == 9:
                        around[i] = 0
                        break
                    else:
                        if k == 0:
                            if mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 6:
                                around[i] = 0
                                break
                        if k == 1:
                            if mini_map[i_tem][j_tem] == 3 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 5:
                                around[i] = 0
                                break
                        if k == 2:
                            if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 4 or mini_map[i_tem][j_tem] == 6:
                                around[i] = 0
                                break
                        elif k == 3:
                            if mini_map[i_tem][j_tem] == 1 or mini_map[i_tem][j_tem] == 2 or mini_map[i_tem][j_tem] == 5:
                                around[i] = 0
                                break
        if around[i] == 9:
            around[i] = 1
    if around == [1, 1, 0, 0]:
        print(i_find + 1, j_find + 1, 1)
    elif around == [0, 1, 1, 0]:
        print(i_find + 1, j_find + 1, 2)
    elif around == [0, 0, 1, 1]:
        print(i_find + 1, j_find + 1, 3)
    elif around == [1, 0, 0, 1]:
        print(i_find + 1, j_find + 1, 4)
    elif around == [1, 0, 1, 0]:
        print(i_find + 1, j_find + 1, '|')
    elif around == [0, 1, 0, 1]:
        print(i_find + 1, j_find + 1, '-')
    elif around == [1, 1, 1, 1]:
        print(i_find + 1, j_find + 1, '+')




