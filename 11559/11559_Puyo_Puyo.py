import sys
sys.stdin = open('11559_Puyo_Puyo.txt')

def simulation(i, j):
    while 1:
        if i + 1 < 12 and mini_map[i + 1][j] == 0:
            mini_map[i + 1][j], mini_map[i][j] = mini_map[i][j], mini_map[i + 1][j]
            i += 1
        else:
            return



def bfs(i, j, color):
    q.append([i, j])
    tem = 0
    while len(q) > tem:
        i, j = q[tem]
        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if ispass(i_tem, j_tem, color) and visited[i_tem][j_tem] == 0:
                visited[i_tem][j_tem] = 1
                q.append([i_tem, j_tem])

        tem += 1

def ispass(i, j, color):
    if -1 < i < 12 and -1 < j < 6 and mini_map[i][j] == color:
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


dummy = [input() for _ in range(12)]
mini_map = [[0 for _ in range(6)] for _ in range(12)]

for i in range(12):
    for j in range(6):
        if dummy[i][j] == 'R':
            mini_map[i][j] = 1
        elif dummy[i][j] == 'Y':
            mini_map[i][j] = 2
        elif dummy[i][j] == 'G':
            mini_map[i][j] = 3
        elif dummy[i][j] == 'B':
            mini_map[i][j] = 4
        elif dummy[i][j] == 'P':
            mini_map[i][j] = 5
cnt = 0
while 1:
    flag = 0
    visited = [[0 for _ in range(6)] for _ in range(12)]

    for i in range(12):
        for j in range(6):
            #값이 들어있고 방문하지 않았다면
            if mini_map[i][j] and visited[i][j] == 0:
                visited[i][j] = 1
                q = []
                bfs(i, j, mini_map[i][j])
                if len(q) >= 4:
                    for a in q:
                        mini_map[a[0]][a[1]] = 0
                    flag = 1

    if flag == 1:
        cnt += 1
        for i in range(10, -1, -1):
            for j in range(6):
                if mini_map[i][j]:
                    simulation(i, j)



    else:
        break

print(cnt)