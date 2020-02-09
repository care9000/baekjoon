import sys
sys.stdin = open('3190_뱀.txt')
import collections

def simulation():
    time = -1

    # 처음방향은 오른쪽
    zz = 0
    dir = 0
    while 1:

        time += 1
        i, j = dummy[-1]
        #만약 미션방향전환 미션에 걸리면?
        for l in range(zz, L):
            if time == int(misions[l][0]):
                if misions[l][1] == 'L':
                    dir += 3
                    dir %= 4
                else:
                    dir += 5
                    dir %= 4
                zz += 1

        nx = i + dx[dir]
        ny = j + dy[dir]

        if is_gameover(nx, ny):
            return time

        if mini_map[nx][ny] == 1:
            dummy.append([nx, ny])
            mini_map[nx][ny] = 0

        else:
            dummy.popleft()
            dummy.append([nx, ny])



def is_gameover(i, j):
    if -1 < i < N and -1 < j < N and [i, j] not in dummy:
        return False

    return True



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#맵의 크기
N = int(input())
mini_map = [[0 for _ in range(N)] for _ in range(N)]

#사과의 갯수
K = int(input())

#사과의 위치

apples = collections.deque(list(map(int, input().split())) for _ in range(K))

#사과를 mini_map 에 위치 시킴
for apple in apples:
    mini_map[apple[0] - 1][apple[1] - 1] = 1

#미션
L = int(input())

#미션의 종류
misions = [input().split() for _ in range(L)]
dummy = collections.deque([])
dummy.append([0, 0])
print(simulation() + 1)
