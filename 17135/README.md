# 제목




## 개요

---

성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. 

## 구현방법

---

미니맵에 적을 배치후 궁수가 쏠 수 있는 몬스터 중에서 가장 왼쪽에 있는 적을 선택후

다선택 된다음에 삭제하고 뒤에있는 적들을 한칸 씩 앞으로 떙겨옴

그리고 만약 적이 없을땐, 함수를 끝내는 식으로 표현하였습니다.

 

## 결과

---

1008ms(3try)

1시간 반

## 회고

---

전에 풀었던 문제였지만 다시플게되니 했갈리는 부분도 많이잇었지만

주어진 조건을 활용하니 쉽게 해결 할 수 있었다.