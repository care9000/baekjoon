import sys
sys.stdin = open('2164_카드2.txt')
import collections
N = int(input())
card_dummy = collections.deque([])
for i in range(1, N + 1):
    card_dummy.appendleft(i)

while len(card_dummy) > 1:
    card_dummy.pop()
    card_dummy.appendleft(card_dummy.pop())

print(card_dummy[0])
