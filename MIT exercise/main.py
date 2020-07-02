from time import *


def border():
    print('\033[1;32m=-=-' * 15)


border()
print('\033[1;32m   Compute the smallest positive integer n for which\n   √(100 + √n) + √(100 - √n) is an integer. ')
border()


def root(n):
    return n ** 0.5


for c in range(1, 10000):
    a = root(100 + root(c))
    b = root(100 - root(c))
    s = int(a + b)
    if a + b == s:
        sleep(1)
        print(f'\033[1;30mExpected response: {c}')
        break
