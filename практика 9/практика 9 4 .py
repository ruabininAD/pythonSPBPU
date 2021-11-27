def sqrt3(value, n, k,r):
    centr = sum(value)/2
    if n-(1/10**r) < centr**k < n+(1/(10**r)): return centr
    if centr**k>n:
        value[1]=value[1]/2
        return sqrt3(value,n, k, r)
    elif centr**k<n:
        value[0]+=value[1]/2
        return sqrt3(value,n,k, r)
    
def main():
    i=int(input("нажмите:  1 - чтобы вычислить корень n степени из числа\n          2 - чтобы возвести число в степень\n"))
    if i ==1:
        n = int(input("введите число "))
        k = float(input("степень корня "))
        r = int(input("число верных знаков "))#порядок точности
        value=[0, n]
        print(f"{n}^(1/{k})==",sqrt3(value, n, k, r))
    elif i ==2:
        n = int(input("введите число "))
        k = float(input("степень числа "))
        r = int(input("число верных знаков "))
        value=[0, n]
        print(f"{n}^{k}==",sqrt3(value, n, 1/k, r))

while True:
    main()
    print("____________________")
