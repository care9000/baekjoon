import sys
sys.stdin = open('3425_고스택.txt')
import collections

def not_is_check():
    if len(stack) < 1:
        return True

    return False


def not_is_check2():
    if len(stack) < 2:
        return True

    return False

while 1:
    information = []
    V = input()
    if V == 'QUIT':
        break

    information.append(V)
    while 1:
        V = input()
        if V != 'END':
            information.append(V)
        else:
            information.append(V)
            break
    N = int(input())
    nums = collections.deque([int(input()) for _ in range(N)])
    while len(nums):
        stack = []
        stack.append(nums.popleft())
        for info in information:
            # NUM 이라면
            if 'NUM' in info:
                stack.append(int(info[4:]))
                if stack[-1] > 1000000000:
                    break
            # POP 이라면
            elif info == 'POP':
                if not_is_check():
                    break
                else:
                    stack.pop()

            # INV라면
            elif info == 'INV':
                if not_is_check():
                    break
                stack[-1] = -(stack[-1])
                if stack[-1] > 1000000000:
                    break

            #DUP라면
            elif info == 'DUP':
                if not_is_check():
                    break
                tem = int(stack.pop())
                stack.append(tem)
                stack.append(tem)


            #SWP라면
            elif info == 'SWP':
                if not_is_check2():

                    break
                else:
                    stack[-2], stack[-1] = stack[-1], stack[-2]

            #ADD 라면
            elif info == 'ADD':
                if not_is_check2():

                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                    if stack[-1] > 1000000000:

                        break

            #SUB 라면
            elif info == 'SUB':
                if not_is_check2():

                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                    if stack[-1] > 1000000000:

                        break

            # MUL 이라면
            elif info == 'MUL':
                if not_is_check2():

                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                    if stack[-1] > 1000000000:

                        break

            elif info == 'DIV':
                if not_is_check2():

                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if b == 0:
                        break

                    elif b * a > 0:
                        stack.append(abs(abs(a) // abs(b)))

                    else:
                        stack.append(-abs(abs(a) // abs(b)))

            elif info == 'MOD':
                if not_is_check2():
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if b == 0:
                        break

                    elif a < 0:
                        stack.append(-abs(abs(a) % abs(b)))

                    else:
                        stack.append(abs(abs(a) % abs(b)))


        if len(stack) != 1 or stack[-1] > 1000000000:
            print('ERROR')

        else:
            print(stack[0])

    input()
    print()


