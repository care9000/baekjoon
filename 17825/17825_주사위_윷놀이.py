import sys
sys.stdin = open('17825_주사위_윷놀이.txt')


def make_scoreboard():
    for i in range(2, 41, 2):
        score_board.append(i)

    for i in range(5):
        score_board.append(0)

    for i in range(4):
        score_board.append(10 + (i * 3))

    for i in range(25, 41, 5):
        score_board.append(i)

    for i in range(5):
        score_board.append(0)

    for i in range(3):
        score_board.append(20 + (i * 2))

    for i in range(25, 41, 5):
        score_board.append(i)

    for i in range(5):
        score_board.append(0)

    score_board.append(30)
    for i in range(3):
        score_board.append(28 - i)

    for i in range(25, 41, 5):
        score_board.append(i)

    for i in range(5):
        score_board.append(0)


def move(horse, location):
    horses[horse] += location
    if horses[horse] == 5:
        horses[horse] = 26

    elif horses[horse] == 10:
        horses[horse] = 39

    elif horses[horse] == 15:
        horses[horse] = 51

    elif 20 < horses[horse] < 26:
        horses[horse] = -1

    elif 33 < horses[horse] < 39:
        horses[horse] = -1

    elif 45 < horses[horse] < 51:
        horses[horse] = -1

    elif 58 < horses[horse]:
        horses[horse] = -1

    elif horses[horse] == 20 or horses[horse] == 33 or horses[horse] == 45:
        horses[horse] = 58

    elif horses[horse] == 30 or horses[horse] == 42:
        horses[horse] = 55

    elif horses[horse] == 31 or horses[horse] == 43:
        horses[horse] = 56

    elif horses[horse] == 32 or horses[horse] == 44:
        horses[horse] = 57

    return score_board[horses[horse]]


def dfs(depth, tem_score):
    global max_result
    if depth == 10:

        if tem_score > max_result:
            max_result = tem_score

        return
    b = 4
    for a in horses:
        if a == 0:
            b -= 1
    if b < 4:
        b += 1
    for k in range(b):
        horse = horses[k]
        if horse != -1:
            i = dice[depth]
            if horse + i == 5:
                if 26 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location
            elif horse + i == 10:
                if 39 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location

            elif horse + i == 15:
                if 51 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location

            elif horse + i == 30 or horse + i == 42:
                if 55 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location

            elif horse + i == 31 or horse + i == 43:
                if 56 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location

            elif horse + i == 32 or horse + i == 44:
                if 57 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location

            elif horse + i == 20 or horse + i == 33 or horse + i == 45:
                if 58 not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location
            else:
                if horse + i not in horses:
                    tem_location = horse
                    dfs(depth + 1, tem_score + move(k, i))
                    horses[k] = tem_location


score_board = [0]
make_scoreboard()
dice = list(map(int, input().split()))
# print(score_board[33: 38], score_board[58], score_board[33])
# print(score_board[20], score_board[33], score_board[45], score_board[59])
horses = [0 for _ in range(4)]
max_result = 0
tem_result = 0
tem_result += move(0, dice[0])
dfs(1, tem_result)

print(max_result)
