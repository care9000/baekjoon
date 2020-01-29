import sys
sys.stdin = open('17836_공주님을_구해라!.txt')


import collections
def bfs(i, j, gram):
    q = collections.deque([])
    q.append([i, j, gram, 1])
    if gram:
        visited_gram[i][j] = 1
        visited_nogram[i][j] = 1
    else:
        visited_nogram[i][j] = 1
    while len(q):
        i, j, gram, time = q.popleft()
        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if ispass(i_tem, j_tem):
                # 그람 획득 했을 경우(벽뚫 가능)
                if gram:
                    if visited_gram[i_tem][j_tem] > time:
                        visited_gram[i_tem][j_tem] = time
                        q.append([i_tem, j_tem, gram, time + 1])
                    if visited_nogram[i_tem][j_tem] > time:
                        visited_nogram[i_tem][j_tem] = time
                else:
                    #벽이면 못감.
                    if mini_map[i_tem][j_tem] != 1:
                        if visited_nogram[i_tem][j_tem] > time:
                            #그람을 볼 경우
                            if mini_map[i_tem][j_tem] == 2:
                                visited_nogram[i_tem][j_tem] = time
                                q.append([i_tem, j_tem, 1, time + 1])
                            else:
                                if visited_nogram[i_tem][j_tem] > time:
                                    visited_nogram[i_tem][j_tem] = time
                                    q.append([i_tem, j_tem, gram, time + 1])







def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        return True
    return False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M, T = map(int, input().split())

mini_map = [list(map(int, input().split())) for _ in range(N)]

visited_nogram = [[T + 1 for _ in range(M)] for _ in range(N)]
visited_gram = [[T + 1 for _ in range(M)] for _ in range(N)]


# 그람획득 여부 체크
gram = 0
if mini_map[0][0] == 2:
    gram = 1
bfs(0, 0, gram)
result = min(visited_nogram[-1][-1], visited_gram[-1][-1])
if T < result:
    print('Fail')
else:
    print(result)