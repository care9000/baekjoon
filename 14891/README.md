# 17135.캐슬디펜스




## 개요

---

총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.

니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

## 구현방법

---

톱니의 위치를 list가 아닌 deque으로 받음(왜냐면 처음것을 뺴고 처음에 추가하기 좋기 때문에)

앞의 [2]와 뒤의 [6]를 비교하여 연결 되어있는지 확인.

그리고 회전시킨다.

 그리고 시계방향 회전이면 마지막것을 뺴서 처음에 넣어줌

반시계방향이면 처음것을 뺴서 마지막에 넣어줌

## 결과

---

76ms(3try)

1시간

## 회고

---

전에 풀었던 문제였지만 다시플게되니 했갈리는 부분도 많았다.

먼저 connent리스트를 초기화 하지않아 틀리게 되었고 

두번째로 그초기화 하지 않은 부분을 늦게 깨달았다.

시험이였으면 넌이미 나가리엿겟지,,ㅠㅠ

집중좀하자.. 시험얼마 안남았다.

처음에 진짜 그지같이 풀었다.

```python
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    magnet = [deque(map(int , input().split())) for _ in range(4)]
    info = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(info)):
        info[i][0] -= 1
    location = [0] * 4
    connect = [0 for _ in range(3)]
    for i in range(len(magnet) - 1):
        if magnet[i][2] != magnet[i + 1][6]:
            connect[i] = 1
    for cnt in range(len(info)):
        if info[cnt][1] == 1:
            tem = magnet[info[cnt][0]].pop()
            magnet[info[cnt][0]].appendleft(tem)
            mini = 0
            for i in range(info[cnt][0] -1, -1, -1):
                mini += 1
                if connect[i] == 1:
                    if info[cnt][1] * (-1) ** mini == 1:
                        tem = magnet[i].pop()
                        magnet[i].appendleft(tem)
                    else:
                        tem = magnet[i].popleft()
                        magnet[i].append(tem)
                else:
                    break
            mini = 0
            for i in range(info[cnt][0], 3):
                mini += 1
                if connect[i] == 1:
                    if info[cnt][1] * (-1) ** mini == 1:
                        tem = magnet[i + 1].pop()
                        magnet[i + 1].appendleft(tem)
                    else:
                        tem = magnet[i + 1].popleft()
                        magnet[i + 1].append(tem)
                else:
                    break
        else:
            tem = magnet[info[cnt][0]].popleft()
            magnet[info[cnt][0]].append(tem)
            mini = 0
            for i in range(info[cnt][0] -1, -1, -1):
                mini += 1
                if connect[i] == 1:
                    if info[cnt][1] * (-1) ** mini == 1:
                        tem = magnet[i].pop()
                        magnet[i].appendleft(tem)
                    else:
                        tem = magnet[i].popleft()
                        magnet[i].append(tem)
                else:
                    break
            mini = 0
            for i in range(info[cnt][0], 3):
                mini += 1
                if connect[i] == 1:
                    if info[cnt][1] * (-1) ** mini == 1:
                        tem = magnet[i + 1].pop()
                        magnet[i + 1].appendleft(tem)
                    else:
                        tem = magnet[i + 1].popleft()
                        magnet[i + 1].append(tem)
                else:
                    break
        for i in range(len(magnet) - 1):
            if magnet[i][2] != magnet[i + 1][6]:
                connect[i] = 1
            else:
                connect[i] = 0
        # [print(magnet[i]) for i in range(len(magnet))]
        # print(connect)
    score = 0
    for i in range(len(magnet)):
        if magnet[i][0] == 1:
            score += 2 ** i
    print("#{} {}".format(tc,score))

```

