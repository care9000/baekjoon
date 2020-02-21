# 4179.불


## 개요

---



지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다. 

불은 각 지점에서 네 방향으로 확산된다. 

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다. 

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.



## 구현방법

---

list 3 개만듬

첫번쨰 리스트는 fire를 담음

두번째 리스트는 지훈이의 위치를 담음

세번쨰 리스트는 출구의 위치를 담음

시뮬레이션 시작!(time 하나씩 증가)

1. fire list를 하나씩 꺼내옴(pop) 
   - 불이 옮겨 붙을 공간(벽이 아니고 불이 없다면)이 나오면 fire_tem에 담아줌 and 그공간을 불로변환
2. 모든 firelist를 pop하면  firelist에 fire_tem에 담긴 것들을 다시 담아줌
3. 지훈이의 위치를 하나씩 꺼내옴(pop)
   - 만약 지훈이가 이동할 공간에 불이 없고 방문한 적이 없다면  jihoon_tem에 담아줌 그리고 vis체크를함
4. 만약 모든 지훈이의 위치를 pop하면 지훈list에 jihoon_tem에 담긴 정보들을 담아줌.
5. 만약 지훈list에 아무것도 담기지 않았다면 지훈이는 이동 불가 이므로 impossble을 return해줌
6. 출구의 위치들을 for문 돌려 만약 출구가 다 불이 옮겨붙으면 impossble을 return해줌
7. 5 or 6번에 해당하지 않는다면 time += 1 해주고 위의 상황을 진행



 

## 결과

---

1시간(5try)

## 회고

---

시간초과가 발생하였는데 5번의 상황을 예외처리 하지 않아 지훈이가 이동 할 수 없음에도 불구하고 계속해서 시뮬레이션을 진행하였기 때문에 시간초과가 났다. 예외처리를 하는것이 반드시 중요하다는 것을 깨닫게 되었다.





```python
import sys
sys.stdin = open('4179_불!.txt')
import collections

def fire_simulation():
    tem_fire_list = []
    while len(fire_list):
        i, j = fire_list.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny):
                tem_fire_list.append([nx, ny])
                mini_map[nx][ny] = 9

    for fire in tem_fire_list:
        fire_list.append([fire[0], fire[1]])


def jihoon_simulation():
    global flag
    tem_jihoon_list = []
    while len(jihoon_list):
        i, j = jihoon_list.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and mini_map[nx][ny] != 9 and vis[nx][ny] == 0:
                if nx == R - 1 or nx == 0 or ny == C -1 or ny == 0:
                    flag = 1
                    return
                tem_jihoon_list.append([nx, ny])
                vis[nx][ny] = 1

    for jihoon in tem_jihoon_list:
        jihoon_list.append([jihoon[0], jihoon[1]])


def ispass(i, j):
    if -1 < i < R and -1 < j < C and mini_map[i][j] == 0:
        return True

    return False

def isnotexit():
    for exit in exit_list:
        if mini_map[exit[0]][exit[1]] == 0:
            return False

    return True



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())

dummy = [input() for _ in range(R)]

mini_map = [[0 for _ in range(C)] for _ in range(R)]

fire_list = collections.deque([])
jihoon_list = collections.deque([])
exit_list = collections.deque([])
for i in range(R):
    for j in range(C):
        if dummy[i][j] == 'F':
            fire_list.append([i, j])
            mini_map[i][j] = 9

        elif dummy[i][j] == 'J':
            jihoon_list.append([i, j])

        elif dummy[i][j] == '#':
            mini_map[i][j] = 1

        if dummy[i][j] != '#' and dummy[i][j] != 'F' and (i == R - 1 or i == 0 or j == C - 1 or j == 0):
            exit_list.append([i, j])

if len(exit_list) == 0:
    print('IMPOSSIBLE ')

else:
    flag = 0
    for exit in exit_list:
        if exit[0] == jihoon_list[0][0] and exit[1] == jihoon_list[0][1]:
            print(1)
            flag = 1
    vis = [[0 for _ in range(C)] for _ in range(R)]
    if flag == 0:
        time = 1
        while 1:
            fire_simulation()
            jihoon_simulation()
            if flag == 1:
                time += 1
                break
            if isnotexit() or len(jihoon_list) == 0 :
                time = - 1
                break
            time += 1
        print(time if time != -1 else 'IMPOSSIBLE ')





```

