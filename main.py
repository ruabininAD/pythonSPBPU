from  random import randint

def su(a,b, c=[]):# слияние двух отсортированных массивов
    lens=len(a)+len(b)
    while len(c) != lens:

        if a == [] or b == []:
            c += (a + b)
            break
        if a[0] > b[0]: c.append(b.pop(0))
        else:   c.append(a.pop(0))

    return c


def buble_sort(arr):
    l = len(arr)

    for i in range(l - 1):
        for j in range(l - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def count_sort(arr):
    m = min(arr)
    counter = [0 for i in range(m, max(arr) + 1)]

    for i in arr:   counter[i - m] += 1#подсчет встреч

    arr.clear()
    for i in counter:
        [arr.append(m) for n in range(i)]
        m += 1
    return arr


def arrR():
    arr=[]
    for i in range(10):
        arr.append(randint(-99, 99))
    return arr


print("Сложение двух сортированных массивов: \nсложность алгоритма O(n+k) \nпотребление памяти  3n\n",su(sorted(arrR()), sorted(arrR())), "\n_______________________\n\n")

print("пузырьковая сортировка: \nсложность алгоритма в худшем случае O(n^2) \nпотребление памяти  n+1\n",buble_sort(arrR()), "\n_______________________\n\n")

print("сортировка подсчетом: \nсложность алгоритма O(n+k)\nгде  k - количество различных чисел в списке \nпотребление памяти  n+k\n",count_sort(arrR()), "\n_______________________\n\n")




