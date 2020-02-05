import sys
import collections
sys.stdin = open('14891_톱니바퀴.txt')


def simulation():
    for act in action:
        connect = [0 for _ in range(3)]
        is_connention(connect)

        move = [0 for _ in range(4)]
        move[act[0] - 1] = act[1]
        # 뒤에꺼 (연결 되어있는지 확인)
        for i in range(act[0] - 1, 3):
            if connect[i] == 1:

                move[i + 1] = - move[i]
            else:
                break

        # 앞에꺼 연결되어 있는지 확인
        for i in range(act[0] - 1, 0, -1):
            if connect[i - 1] == 1:

                move[i - 1] = - move[i]

            else:
                break

        for k in range(4):
            if move[k] == 1:
                clockwise(k)

            elif move[k] == -1:
                anticlockwise(k)



def is_connention(connect):
    for i in range(3):
        if gear[i][2] != gear[i + 1][6]:
            connect[i] = 1


def clockwise(num):
    gear[num].appendleft(gear[num].pop())
    return


def anticlockwise(num):
    gear[num].append(gear[num].popleft())
    return


dummy = [input() for _ in range(4)]

gear = list(collections.deque([]) for _ in range(4))

for i in range(4):
    for j in range(8):
        gear[i].append(int(dummy[i][j]))

K = int(input())
action = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]





simulation()

result = 0
for i in range(4):
    if gear[i][0] == 1:
        result += 2 ** i

print(result)