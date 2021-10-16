def n1():
    print("какая скорость?")
    v= int(input())
    print("сколько часов оно двигалось?")
    t = int(input())
    print("час    пройденное расстяние")
    print("=======================")
    for i in range (1,t+1):
        print(i, "   ", i*v)    
    end() 
        
def n2():
    
    print("начните вводить числа")
    i = int(input())
    s= i
    while i > 0:
        i = int(input())
        if i >0:
            s += i
        else:   break
        #print(i , "    ", s)
    print("их сумма = ", s)
    end() 

def n3():
    print("введите число")
    i =int(input())
    s= 1
    while i>1:
        s=s*i
        i=i-1
    print(s)
    end() 
    
def n4():
    print("стартовое количество")
    i = int(input())
    print("среднесуточное увеличение")
    r = int(input())
    r = (r/100) + 1
    print("количество дней для размножения")
    w = int(input())
    print(" день   популяция")
    
    for o in range(1,w+1):
        print(o, ' '* (10-len(str(o))),  round(i*r**(o-1), 3))
    end() 
    
def n5():
    print("введите высоту")
    h = int(input())
    for i in range(1,h+1):
        print("#"," "*(i-1),"#", sep="")
    end()          
              
              
def end():    
    print("для возвращения к выборy задачи нажмите 0")
    print("для завершения нажмите 9")
    i=str(input())
    if i =="0":
        nom()
    if i =="9":
        sys.exit()
        
def nom():
    print("введите номер задачи")
    i = int(input())
    if i == 1:  n1()
    if i == 2:  n2()
    if i == 3:  n3()
    if i == 4:  n4()
    if i == 5:  n5()
nom()  
    
    