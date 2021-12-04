import sys
import time
sys.setrecursionlimit(30000)


def fib_line(n):

    if n in (1, 2):
        return 1
    return fib_line(n - 1) + fib_line(n - 2) #сложность О(2^n)


def fib_cache(a, n): # Сложность O(n)

    a.append(a[-1]+a[-2])

    if len(a)==n:   return (a[-1])
    else:   return fib_cache(a, n)


def fib_loop(a,n):
    while len(a)!=n:    a.append(a[-1]+a[-2])
    return(a[-1])



a=[1,1]
n=1340


n = int(input("введите номер числа фибоначи для \nрекурсивного алгоритма с кешем: "))
first = time.time()
print(fib_cache(a,n))
seconds = time.time()
print(seconds-first)

n = int(input("введите номер числа фибоначи для \nлинейного рекурсивного алгоритма: "))
first = time.time()
print(fib_line(n))
seconds = time.time()
print(seconds-first)

a=[1,1]
n = int(input("введите номер числа фибоначи для \nцикличного алгоритма: "))
first = time.time()
print(fib_loop(a, n))
seconds = time.time()
print(seconds-first)

