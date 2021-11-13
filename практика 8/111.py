import argparse
import random

def head(name_file):
    
    try:
        with open(name_file, 'r') as f:
            with open(name_file, 'r') as f:
                nums = f.read().splitlines()
                for i in range(10):   print( (nums[i]))
    except IOError: print("File not accessible")
    except Exception:   print("проверь аргумент")
    
    
    
    
    
def konkatenation(a, b):
    try:
        with open(a, 'r') as f:    nums = f.read().splitlines()
        for i in nums:    print(i)
        with open(b, 'r') as f:    nums = f.read().splitlines()
        for i in nums:    print(i)
    except IOError:
        print("File not accessible")
    except Exception:   print("проверь аргумент")
        

def giv_nonber(a, new_name):
    try:
        texx=""
        k = 1
        with open(a, 'r') as f:    nums = f.read().splitlines()
        for i in nums:
            texx+=str(k)+": "+i+"\n"
            k+=1
        with open(new_name, 'w') as f:    f.write(texx)
    except IOError: print("File not accessible")
    except Exception:   print("проверь аргумент")

def very_big(m):
    try:
        texx=[]
        with open(m, 'r') as f:    nums = f.read().splitlines()
        for i in nums:  texx.extend(i.split())
        texx=list(reversed(sorted(texx, key=len)))
        len_max=len(texx[0])
        for i in texx:
            if len(i)==len_max: print(i)
            else:   break
    except IOError: print("File not accessible")
    except Exception:   print("проверь аргумент")
    
def pasword(w):
    try:
        texx=[]
        with open(w, 'r') as f:    nums = f.read().splitlines()
        for i in nums:  texx.extend(i.replace("\n", '').strip().split(", "))
        count=len(texx)
        texx=random.sample(texx, 2)
        new_texx=[i.title()  for i in texx]
        [print(i, end="") for i in new_texx]
    except IOError: print("File not accessible")
    except Exception:   print("проверь аргумент")


def comm(w):
    try:
        def_count,count_com=0, 0
        texx=[]
        with open(w, 'r') as f:    nums = f.read().splitlines()
        for i in nums:  
            if "def " in i:
                def_count+=1
                if k!="" and k[0]=="#": count_com+=1
            k=i
            
        if def_count==0: print("нет функций") 
        elif count_com<def_count :    print("не все функции не пояснены")
        elif count_com==def_count:    print("все функции пояснены ") 
        
    except IOError: print("File not accessible")
    except Exception:   print("проверь аргумент")





parser = argparse.ArgumentParser()
parser.add_argument("-_name", type=str, help="file name")
parser.add_argument("-nomber", "--action", type=int, help="comand nomber")
parser.add_argument("-sec_file", "--second_file", type=str, help="second file name", required=False)
args = parser.parse_args()


if args.action ==1:    head(args._name) #выдача 10 строк
elif args.action ==2:    konkatenation(args._name, args.second_file)
elif args.action ==3:    giv_nonber(args._name, args.second_file)
elif args.action ==4:    very_big(args._name)
elif args.action ==5:   pasword(args._name)
elif args.action ==6:   comm(args._name)



