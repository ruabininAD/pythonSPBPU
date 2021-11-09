import sys
sys.setrecursionlimit(10000)

def print_till_zero(n):
    if n !=0:
        print(n)
        n-=1
        return print_till_zero(n)

def s_palindrome(s): # ДЛЯ СТРОК И ПРЕДЛОЖЕНИЙ
    s=s.replace(" ","")
    flag = True
    if len(s)>1:
        if  s[0]!=s[-1]:
            flag = False
            return False
        s=s[1:-1]
        return s_palindrome(s)
    return flag

def power(a, n):
    if n>1:
        if n%2==1:  return ( power(a, n-1) * a)
        else:       return ( power(a, n/2) * power(a, n/2))
    else:           return a



def  max_in(lizt):
    if lizt[0] > lizt[-1]:      return max_in(lizt[:-1])
    elif lizt[0] < lizt[-1]:    return max_in(lizt[1:])
    else:
        if len(lizt)==1:        return lizt[0]
        else:                   return max_in(lizt[:-1])

#print(max_in([2,1,2,3,4,5,6,5,4,5,4,3,2,1,6,7,54,3,6,123,3,2,3,4,2]))

def hanoi(n, x=1, y=3):
    if n == 1:  print(f'Переложит диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        hanoi(n - 1, x, 6 - x - y)
        print(f'Переложит диск {n} со стержня номер {x} на стержень номер {y}')
        hanoi(n - 1, 6 - x - y, y)


def check():
    print("задача 1")
    print_till_zero( n=int(input("введи число: " )) )     #111111
    print("задача 2", "\n")
    print( s_palindrome( s =str(input("введи строку: "))))   #222222
    print("задача 3", "\n")
    print(  power( a =int(input("введи число: ")),  n =int(input("введи степень: "))) )           #333333


    array=[2,1,2,3,4,5,6,5,4,5,4,3,2,1,6,7,54,3,6,123,3,2,3,4,2]


    print("задача 4", "\n")
    print( max_in(array)) #44444
    print("задача про Ханою", "\n")
    hanoi(n = int(input('Введите количество дисков:')))

check()