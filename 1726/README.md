# 1726.로봇


## 개요

---



많은 공장에서 로봇이 이용되고 있다. 우리 월드 공장의 로봇은 바라보는 방향으로 궤도를 따라 움직이며, 움직이는 방향은 동, 서, 남, 북 가운데 하나이다. 로봇의 이동을 제어하는 명령어는 다음과 같이 두 가지이다.

명령 1. Go k
 \- k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.

명령 2. Turn dir
 \- dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.

공장 내 궤도가 설치되어 있는 상태가 아래와 같이 0과 1로 이루어진 직사각형 모양으로 로봇에게 입력된다. 0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점이고, 1은 궤도가 없어 로봇이 갈 수 없는 지점이다. 로봇이 (4, 2) 지점에서 남쪽을 향하고 있을 때, 이 로봇을 (2, 4) 지점에서 동쪽으로 향하도록 이동시키는 것은 아래와 같이 9번의 명령으로 가능하다.

로봇의 현재 위치와 바라보는 방향이 주어졌을 때, 로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램을 작성하시오.

## 구현방법

---

bfs로 구현하였으며 2가지 경우로 나누었다.

1. 명령 1 go k  k만큼 이동 (그러나 벽일경우 중단)

   - ```python
             for move in range(1, 4):
                 i_tem = i + (move * dx[dir])
                 j_tem = j + (move * dy[dir])
                 if ispass(i_tem, j_tem):
                     if vis[i_tem][j_tem][dir] > cnt + 1:
                         vis[i_tem][j_tem][dir] = cnt + 1
                         q.append([i_tem, j_tem, dir, cnt + 1])
                 else:
                     break
     ```

   - 

2. turn dir

   - 방향회전

     ```python
             if dir > 2:
                 for dir_tem in range(1, 3):
                     if vis[i][j][dir_tem] > cnt + 1:
                         vis[i][j][dir_tem] = cnt + 1
                         q.append([i, j, dir_tem, cnt + 1])
     
             else:
                 for dir_tem in range(3, 5):
                     if vis[i][j][dir_tem] > cnt + 1:
                         vis[i][j][dir_tem] = cnt + 1
                         q.append([i, j, dir_tem, cnt + 1])
     
     ```

     

 

## 결과

---

1시간

## 회고

---

1번경우에서 break를 걸어주지 않아 벽이있을떄 뛰어넘어가는 현상이 발생하였는데 수정하였습니다.

