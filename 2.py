# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
rank = []
for j in range(N * (N - 1)):
    game = list(input().split())
    a = 0
    for k in rank:
        if game[0] == k[0]:
            a = 1
            break

    if a == 0:
        # 이겻을 경우
        if game[1] == '2':
            rank.append([game[0], 1, int(game[1]), int(game[3])])
        # 질경우
        else:
            rank.append([game[0], 0, int(game[1]), int(game[3])])

    else:
        for i in range(len(rank)):
            if rank[i][0] == game[0]:
                if game[1] == '2':
                    rank[i][1] += 1

                rank[i][2] += int(game[1])
                rank[i][3] += int(game[3])
                break
    a = 0
    for k in rank:
        if game[2] == k[0]:
            a = 1
            break
    if a == 0:
        # 이겻을 경우
        if game[3] == '2':
            rank.append([game[2], 1, int(game[3]), int(game[1])])
        # 질경우
        else:
            rank.append([game[2], 0, int(game[3]), int(game[1])])

    else:
        for i in range(len(rank)):
            if rank[i][0] == game[2]:
                if game[3] == '2':
                    rank[i][1] += 1

                rank[i][2] += int(game[3])
                rank[i][3] += int(game[1])
                break
result = []
for r in rank:
    result.append([r[1], r[2] - r[3], r[0]])
result.sort(reverse=True)

for i in range(N - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if result[i][0] == result[j][0] and result[i][1] == result[j][1]:
            data = [result[i][2], result[j][2]]
            data.sort()
            if data[0] == result[i][2]:
                result[i], result[j] = result[j], result[i]
for re in result:
    print("{} {} {}".format(re[2], re[0], re[1]))