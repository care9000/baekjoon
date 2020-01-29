# 2171_로봇 시뮬레이션_

- URL: https://www.acmicpc.net/problem/2174

- 출처:[ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [Europe ](https://www.acmicpc.net/category/10)> [Northwestern European Regional Contest ](https://www.acmicpc.net/category/15)> [Nordic Collegiate Programming Contest ](https://www.acmicpc.net/category/46)> [NCPC 2005](https://www.acmicpc.net/category/detail/216) A번


## 개요

---

로봇의 초기 위치를 주워지고, 수행 할 미션을 주어진다. 

1. L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
2. R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
3. F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.

미션을 수행도중 

1. Robot X crashes into the wall: X번 로봇이 벽에 충돌하는 경우이다. 즉, 주어진 땅의 밖으로 벗어나는 경우가 된다.
2. Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우이다.

이러한 경우가 있다.

이러한 상황 속에 시뮬레이션 결과값을 구하기 

## 구현방법

---

시뮬레이션이였기 때문에 주어진 순서대로 진행하였다.

처음 데이터를 받고 가공을 하였다 왜냐면 F,  L, R, 을 인트로 바꿔주기 위해서 그리고 방향들도 데이터를 받았다. 

그리고 시뮬레이션에 들어갔다. 그리고 3가지의 경우를 나눠서 계산하였다.

먼저 방향이 L 이면 좌측으로 방향을 바꾸고

방향이 R 이면 우측으로 방향을 바꾸고 

F면 방향대로 직진을 하였다. 한번 직진을 하고 나서 벽을 만났는지, 다른 로봇과의 충돌은 없었는지 파악을 했다. 만약 충돌을 하거나 벽을 만나면 출력값에 맞게 출력하였다.

 

## 결과

---

푸는데 총 소요시간 (코딩:1시간9분)

2번 시도 

## 회고

---

- 시뮬레이션이여서 주어진 조건대로 하였다. 하지만 처음엔 틀렸다.

  -  그이유는 N 방향과 S방향에 대해 제대로 이해하지 않았기 때문이였다.

- 실수는 더더욱하면 안되겠지만 예제 케이스 가 다맞다고 제출하는 것이 아니라 내가 간단한 예제 케이스를 만들어 제출하는 과정을 해봐야할것 같다 ㅠㅠ.

  