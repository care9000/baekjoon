# 2151.거울 설치


## 개요

---



채영이는 거울을 들여다보는 것을 참 좋아한다. 그래서 집 곳곳에 거울을 설치해두고 집 안을 돌아다닐 때마다 거울을 보곤 한다.

채영이는 새 해를 맞이하여 이사를 하게 되었는데, 거울을 좋아하는 그녀의 성격 때문에 새 집에도 거울을 매달만한 위치가 여러 곳 있다. 또한 채영이네 새 집에는 문이 두 개 있는데, 채영이는 거울을 잘 설치하여 장난을 치고 싶어졌다. 즉, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어졌다.

채영이네 집에 대한 정보가 주어졌을 때, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수를 구하는 프로그램을 작성하시오.

거울을 설치할 때에는 45도 기울어진 대각선 방향으로 설치해야 한다. 또한 모든 거울은 양면 거울이기 때문에 양 쪽 모두에서 반사가 일어날 수 있다. 채영이는 거울을 매우 많이 가지고 있어서 거울이 부족한 경우는 없다고 하자.

거울을 어떻게 설치해도 한 쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다.



## 구현방법

---

vis = 3차원으로 받게함.

거울을 설치 할 수 있을떄는 설치하거나 안하게함

설치할 경우에는 cnt 를 하나 증가시키고 방향전환시키고 append

설치를 안할 경우에는 cnt는 그대로 하고 appendleft해줌

만약 도착점에 도착하면 return cnt를 함.

 

 

## 결과

---

1시간

4try

80ms

## 회고

---

3차원으로 받아서 방향에따라 리스트에 vis를 체크함 vis를 체크하는 경우 cnt를 증가시켜주지 않으면 left에 추가하였다. 이유는 최소 cnt를 출력해야 하기 떄문에 했고 비슷한 유형을 전에 풀어 봐서 사용하는데 어려움이 없었다.

핵심은 방향에 따라 vis를 체크하는게 중요한 것 같다.