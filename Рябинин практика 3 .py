import random
 #ПРАКТИКА 3
"""запустите программу
инструкии будут выведены в консоль"""
def n1():
    print("задача 1. определение четности или нечетности числа")
    print("Введите число")
    i = int(input())
    if i/2  == i//2:
        print(i, " четное число")
    else:
        print(i, " нечетное число")
    
def n2():
    print("задача 2. перевод из цельсий в фаренгейт")
    print("введите градусы цельсия для перевода в фарегнейт")
    c = int(input())
    print (c, " градусов = ",(c*9/5)+32, " фаренгейт")

def n3():
    print("задача 3. делимость числа на 5 и 7")
    print("введите число")
    i = int(input())
    if i%5!=0 and i%7!=0:
        print("00")
    elif i%5==0 and i%7!=0:
        print("01")
    elif i%5!=0 and i%7==0:
        print("10")
    elif i%5==0 and i%7==0:
        print("11")

def n4():
    print("задача 4. квычисление корней квадратного уравнения")
    print("ax^2 +bx +c = 0")
    print("введите a,b,c через пробел в одну строку")
    
    a, b, c=input().split(" ")
    a, b, c = int(a), int(b), int(c)
    print("(", a, ")x^2 +(",b,")x +(",c,") = 0", sep="")
    d=b**2 - 4*a*c
    if d>0:
        print("х=", (-b+(d)**0.5)/(2*a) )
        print("х=", (-b-(d)**0.5)/(2*a) )
    elif d==0:
        print("х=", -b/ (2*a) )
    else:
        print("нет корней")

def n5():
    print("задача 5. игра, нахождение случайного числа")
    print("ведите n")
    n = int(input())
    print("ведите k")
    k = int(input())
    a=random.randint(1 , n )
    i, w =1, 0
    print("игра началась \nкомпьютер загадал число \nугадай его")
    while i<k+1 and  w!=a:
        print("введите число")
        w=int(input())
        if w==a:
            print("Вы угадали")
            break
        elif w>a:
            print("Загаданное число меньше")
        elif w<a:
            print("Загаданное число больше")
        i+=1

def n6():
    print("введите через пробел элименты списка")
    a = [i for i in input().split()]
    #print(a)
    b=[]
    for i in range(0,len(a)):
        #print("i",i,"a[i]", a[i])
        if a[i] not in b:
            b.append(a[i])
            #print('a',a,"b", b)
        else:   continue
    print(len(b))
        
def n7():
    cube=[[[0 for i in range(3)] for j in range(3)] for k in range(3)]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print("введите значение в (",i+1,j+1,k+1,")")
                x = int(input())
                cube[i][j][k]=x
    print ("( x , y, z )")
    
    for i in range(3):
        for j in range(3):
            if cube[i][j][0]+cube[i][j][1]+cube[i][j][2] == 0: 
                print("(",i+1,";",j+1,";","( 1, 2, 3)", ")")
    
    for j in range(3):
        for k in range(3):
            if cube[0][j][k]+cube[1][j][k]+cube[2][j][k] == 0: 
                print("(","( 1, 2, 3 )",";", j+1,";",k+1,")")
            
    for k in range(3):
        for i in range(3):
            if cube[i][0][k]+cube[i][1][k]+cube[i][2][k] == 0: 
                print("(",i+1,";","( 1,2,3 )",";",k+1, ")")




print("введите номер задачи")
i = int(input())
if i == 1:  n1()
if i == 2:  n2()
if i == 3:  n3()
if i == 4:  n4()
if i == 5:  n5()
if i == 6:  n6()
if i == 7:  n7()



