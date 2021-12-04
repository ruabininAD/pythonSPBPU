#интерполяционный поиск
import sys
import time

#Интерполяционный поиск работает быстрее.

def bin_recurs(arr, n):
    i = len(arr)//2
    k = arr[i] #значениесерединног
    if n > k:   return bin_recurs(arr[i:], n)
    elif n < k: return bin_recurs(arr[:i], n)
    elif k == n:    return True




def inter_search(lst, item):
    start= 0
    stop = len(lst)-1
    result = False

    while (start<=stop and item >=lst[start]) and item<=lst[stop] and not result:

        midlle = start + int(((stop - start)/(lst[stop]-lst[start]))*(item - lst[start]))
        app_element = lst[midlle]

        if app_element == item: result = True

        if app_element < item:  start = midlle +1

        else:   stop = midlle - 1

    return result



lens = int(input("введите длину массива: 10^ "))
lst = [i for i in range(1, 10**lens)]
sys.setrecursionlimit(10 ** lens)


value = int (input(f"Введите число для поиска от 1 до 10^{lens}: "))
print()


start_time = time.time()
print("интерполяционный поиск. Результат: ", inter_search(lst, value))
print("интерполяционный поиск. Время: ", time.time() - start_time)
print()

start_time = time.time()
print("Бинарный поиск. Результат: ", bin_recurs(lst, value))
print( "Бинарный поиск. Время: ", time.time() - start_time)