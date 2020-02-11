# 14890.경사로


## 개요

---



길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

- 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
- 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
- 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.

아래와 같은 경우에는 경사로를 놓을 수 없다.

- 경사로를 놓은 곳에 또 경사로를 놓는 경우
- 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
- 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
- 경사로를 놓다가 범위를 벗어나는 경우



## 구현방법

---

내위치 와 내앞위치를 비교

1. 내위치가 이전보다 오르막일 경우
   - 이전(L)만큼 비교,  L이전값은 벽 or 이전값들보다 작거나 같아야함.
2. 이전보다 내리막일 경우
   - 앞으로(L) 만큼 비교, 그다음은 벽 or 이전값보다 크거나 같아야함.
3. 이전과 같은 경우 
   - 계속 진행

## 결과

---

64ms(1try)

2시간 구현



## 회고

---

생각보다 쉬운 구현이였으나. 왜 처음에 생각을 잘못했는지 이해 할 수 없었다. 앞것들만 비교하고 그앞을 비교하지 않거나 뒤에꺼만 비교하고 그뒤는 비교하지 않아 예제 케이스가 틀리게 나오는 경우가 많이 발생하였다. 이런 부분은 진짜 고쳐야 할 점이다.