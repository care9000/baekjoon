import sys
sys.stdin = open('14499_주사위_굴리기.txt')

def simulation(i, j):
    for order in orders:
        if is_pass(i, j, order):
            i += dx[order]
            j += dy[order]
            is_change(order)
            if mini_map[i][j] == 0:
                mini_map[i][j] = dice[2]

            else:
                dice[2] = mini_map[i][j]
                mini_map[i][j] = 0

            print(dice[5])


def is_change(order):
    if order == 1:
        dice[5], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[5]

    elif order == 2:
        dice[2], dice[3], dice[5], dice[1] = dice[1], dice[2], dice[3], dice[5]

    elif order == 3:
        dice[2], dice[4], dice[5], dice[0] = dice[0], dice[2], dice[4], dice[5]

    else:
        dice[5], dice[0], dice[2], dice[4] = dice[0], dice[2], dice[4], dice[5]





def is_pass(i, j, order):
    i_tem = i + dx[order]
    j_tem = j + dy[order]
    if -1 < i_tem < N and -1 < j_tem < M:
        return True
    return False
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


N, M, x, y, K = map(int, sys.stdin.readline().split())
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
orders = list(map(int, sys.stdin.readline().split()))
# print(orders)

dice = [0 for _ in range(6)]
# 주사위 1,
#     2, 3, 4
#       5,
#        6

simulation(x, y)