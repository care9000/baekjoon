import sys
sys.stdin = open('3055_탈출.txt')
import collections

def simulation():
    global time

    while 1:
        time += 1
        for i in range(R):
            for j in range(C):
                if Tishun_Forest[i][j] == 1:
                    for k in range(4):
                        i_tem = i + dx[k]
                        j_tem = j + dy[k]
                        if -1 < i_tem < R and -1 < j_tem < C and Tishun_Forest[i_tem][j_tem] == 0:
                            Tishun_Forest[i_tem][j_tem] = 99
        for i in range(R):
            for j in range(C):
                if Tishun_Forest[i][j] == 99:
                    Tishun_Forest[i][j] = 1
        flag = 0
        for k in range(4):
            i_tem = Beaver_House[0] + dx[k]
            j_tem = Beaver_House[1] + dy[k]
            if -1 < i_tem < R and -1 < j_tem < C and (Tishun_Forest[i_tem][j_tem] != 1 or Tishun_Forest[i_tem][j_tem] != 2):
                flag = 1
                break
        if flag == 0:
            time = -1
            return

        q = []
        # print(Hedgehog_location)
        while len(Hedgehog_location):
            tem = Hedgehog_location.popleft()
            Tishun_Forest[tem[0]][tem[1]] = 0
            for k in range(4):
                i_tem = tem[0] + dx[k]
                j_tem = tem[1] + dy[k]
                if -1 < i_tem < R and -1 < j_tem < C and (Tishun_Forest[i_tem][j_tem] == 0 or Tishun_Forest[i_tem][j_tem] == 8) and visited[i_tem][j_tem] == 0:
                    visited[i_tem][j_tem] = 1
                    q.append([i_tem, j_tem])
                    if i_tem == Beaver_House[0] and j_tem == Beaver_House[1]:
                        return
        if len(q) == 0:
            time = -1
            return
        for i in range(len(q)):
            Hedgehog_location.append([q[i][0], q[i][1]])
        # print(Hedgehog_location)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())
dummy = [input() for _ in range(R)]
Tishun_Forest = [[0 for _ in range(C)] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
# 물 은 1  돌은 2 비버의 굴 8 고슴도치 9

Hedgehog_location = collections.deque([])
Beaver_House = []
for i in range(R):
    for j in range(C):
        if dummy[i][j] == '*':
            Tishun_Forest[i][j] = 1
        elif dummy[i][j] == 'X':
            Tishun_Forest[i][j] = 2
        elif dummy[i][j] == 'D':
            Tishun_Forest[i][j] = 8
            Beaver_House.append(i)
            Beaver_House.append(j)
        elif dummy[i][j] == 'S':
            Tishun_Forest[i][j] = 9
            Hedgehog_location.append([i, j])

time = 0
visited[Hedgehog_location[0][0]][Hedgehog_location[0][1]] = 1


simulation()
if time == -1:
    print("KAKTUS")
else:
    print(time)



