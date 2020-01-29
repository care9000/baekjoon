import sys
sys.stdin = open('2171_로봇_시뮬레이션.txt')

def start():
    for simulation in simulations:
        for attempt in range(simulation[2]):
            # 명령어가 0인지 -1인지 1인지 파악
            if simulation[1] == 0:
                robots[simulation[0] - 1][0] += dx[robots[simulation[0] - 1][2]]
                robots[simulation[0] - 1][1] += dy[robots[simulation[0] - 1][2]]

                if iswall(robots[simulation[0] - 1][0], robots[simulation[0] - 1][1]):
                    print('Robot {} crashes into the wall'.format(simulation[0]))
                    return
                if iscrash(simulation[0] - 1):
                    print('Robot {} crashes into robot {}'.format(simulation[0], heart[0] + 1))
                    return

            elif simulation[1] == -1:
                robots[simulation[0] - 1][2] -= 1
                robots[simulation[0] - 1][2] += 4
                robots[simulation[0] - 1][2] %= 4
            else:
                robots[simulation[0] - 1][2] += 1
                robots[simulation[0] - 1][2] += 4
                robots[simulation[0] - 1][2] %= 4

    print('OK')
#벽인지 아닌지 파악
def iswall(i, j):
    if -1 < i < B and -1 < j < A:
        return False
    return True

#충돌 했는지 안했는지 파악
def iscrash(i):
    for j in range(len(robots)):
        if i != j:
            if robots[i][0] == robots[j][0] and robots[i][1] == robots[j][1]:
                heart.append(j)
                return True
    return False

#네방향 움직임
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


A, B = map(int, input().split())
N, M = map(int, input().split())

dummys = [list(input().split()) for _ in range(N)]
dummys2 = [list(input().split()) for _ in range(M)]

simulations = []
# 직진은 0, 왼쪽 90는 -1 오른쪽 90은 1
for dummy2 in dummys2:
    if dummy2[1] == 'F':
        simulations.append([int(dummy2[0]), 0, int(dummy2[2])])
    elif dummy2[1] == 'L':
        simulations.append([int(dummy2[0]), - 1, int(dummy2[2])])
    else:
        simulations.append([int(dummy2[0]), 1, int(dummy2[2])])


robots = []


# 네방향 ( 북, 동, 남, 서) 0, 1, 2, 3
for dummy in dummys:
    if dummy[2] == 'E':
        robots.append([int(dummy[1]) - 1, int(dummy[0]) - 1, 1])
    elif dummy[2] == 'W':
        robots.append([int(dummy[1]) - 1, int(dummy[0]) - 1, 3])
    elif dummy[2] == 'N':
        robots.append([int(dummy[1]) - 1, int(dummy[0]) - 1, 0])
    else:
        robots.append([int(dummy[1]) - 1, int(dummy[0]) - 1, 2])

heart = []
start()