# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:03:42 2021

@author: ryabi
"""


w = "habr.py"


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
    except Exception:
        print("проверь аргумент")
comm(w)
