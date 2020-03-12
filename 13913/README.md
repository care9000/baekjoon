# 13913.숨바꼭질


## 개요

---



수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 구현방법

---

bfs로 location - 1, location + 1, location * 2를 확인한 후 맞는 조건이 나오면 그자리에 visited를 찍었다.

그리고 나서 함수가 끝난후 while 문을 돌려 이떄까지 지나온 경로를 list에 append했다.

 

## 결과

---

1시간

## 회고

---

틀린방법: 찾으러 갈때 이때까지 온 것들과 time 을 같이 넘겨주게 하였다. 그러다보니 당연히 시간도 오래걸리고 찾는양도 많아져 시간초과가 났었다.

하지만 예전에 푼 거의최단 경로 문제를 떠올리니 일단 visi를 찍고 나중에 visted[k] - 1 의 값과 같은 것을 찾기로 하였다. 그러다 보니 자연스럽게 맞출 수 있게 되었다,

시간초과 문제는 어떻게 해결해야 할지 감이 안오는거 같다. ㅠㅠ