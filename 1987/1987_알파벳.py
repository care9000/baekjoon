import sys
sys.stdin = open('1987_알파벳.txt')

import collections

#
# def dfs(i, j):
#     global result
#     if result == max_length:
#         return
#     if result < len(bank):
#         result = len(bank)
#     for k in range(4):
#         i_tem = i + dx[k]
#         j_tem = j + dy[k]
#         if -1 < i_tem < R and -1 < j_tem < C and data[i_tem][j_tem] not in bank:
#             bank.append(data[i_tem][j_tem])
#             dfs(i_tem, j_tem)
#             if result == max_length:
#                 return
#             bank.pop()
def dfs(i, j, cnt):
    global result
    if result == max_length:
        return
    if cnt > result:
        result = cnt
    for k in range(4):
        i_tem = i + dx[k]
        j_tem = j + dy[k]
        if -1 < i_tem < R and -1 < j_tem < C and info[ord(data[i_tem][j_tem]) - 65] == 0:
            info[ord(data[i_tem][j_tem]) - 65] = 1
            dfs(i_tem, j_tem, cnt + 1)
            info[ord(data[i_tem][j_tem]) - 65] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



R, C = map(int, input().split())
data = [input() for _ in range(R)]
dummy = [0 for _ in range(26)]
cnt = 0
for i in range(R):
    for j in range(C):
        dummy[ord(data[i][j]) - 65] = 1

for i in range(26):
        if dummy[i] == 1:
            cnt += 1


max_length = cnt
result = 0

info = [0 for _ in range(26)]
info[ord(data[0][0]) - 65] = 1
dfs(0, 0, 1)
print(result)