import sys
sys.stdin = open('18808_스티커_붙이기.txt')
import collections

def turn0(R, C, )

#
# def simulation():
#     R, C, sticker = Stickers.popleft
#     for move in range(4):
#


N, M, K = map(int, input().split())
mini_map = [[0 for _ in range(M)] for _ in range(N)]
Stickers = collections.deque([])
for _ in range(K):
    R, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(R)]
    Stickers.append([R, C, data])


while 1:
    R, C, sticker = Stickers.popleft()

    if turn0(R, C, sticker):
        break

