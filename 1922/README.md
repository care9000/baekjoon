# 1922_네트워크_연결


## 개요

---



1. 도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다. 하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다. 그런데 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다. (a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다. a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)

   그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야 컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다. 이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 모든 컴퓨터를 연결할 수 없는 경우는 없다.



## 구현방법

---

크루스칼 알고리즘을 이용하여 풀려고 했다.

먼저 길이가 작은 순 대로 리스트에 담아줬고 

크루스칼 알고리즘을 통하여 PI가 다를 경우에는 PI값이 낮은 것으로 통합 시켜주었다.

 

## 결과

---

4000ms



## 회고

---

크루스칼 알고리즘을 공부하기 위해 문제를 풀어봤다. 