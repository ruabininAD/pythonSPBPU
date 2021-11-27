import time
import random
import sys


arr = []
lens = int(input("введите длину массива: 10^ "))
[arr.append(random.randint(1, 10 ** lens)) for i in range(10 ** lens)]
sys.setrecursionlimit(10 ** lens)


def line_search(arr, n):
    for i in arr: 
        if i == n:  return True
        if i !=n:   pass
            
def bin_search(arr, n):
    arr = sorted(arr)
    #i = len(arr)//2 #индекс серединного элимента
    #k = arr[i] #значениесерединногоэдимента
    #print(arr)
    while True: # пока серединное значение не равно искомому
        i = len(arr)//2
        k = arr[i] #значениесерединного
        if n > k:   arr = arr[i:]# если искомое больше серединного
        elif n < k: arr = arr[:i]
        elif k == n:    break

def recurs(arr, n):
    i = len(arr)//2
    k = arr[i] #значениесерединног
    if n > k:   return recurs(arr[i:], n)
    elif n < k: return recurs(arr[:i], n)
    elif k == n:    return True


start_time = time.time()
n = arr[-1]
line_search(arr, n)
line_time = time.time() - start_time
print("Линейный поиск: ", line_time, "секунд")


start_time = time.time()
n = max(arr)
bin_search(arr, n)
bin_time = time.time() - start_time
print("Бинарный поиск: ", bin_time, "секунд")

start_time = time.time()
arr=sorted(arr)
recurs(arr, n)
recurs_time = (time.time() - start_time)
print("Бинарный поиск по рекурсии: ", recurs_time, "cекунд")
