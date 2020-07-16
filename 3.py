import collections

N, K = map(int, input().split())
snacks = [float(input()) for _ in range(N)]
snacks.sort()
while len(snacks) != K:
    longest_snack= snacks.pop()
    i = 1
    while longest_snack / i > snacks[0]:
        i += 1
    # 1이 아닐떄
    if i > 2:
        tem = longest_snack / (i - 1)

        for j in range(i - 1):
            snacks.append(round(tem, 2))
    # 1 일때
    else:
        tem = longest_snack / 2
        for j in range(2):
            snacks.append(round(tem, 2))
    snacks.sort()

print(snacks)