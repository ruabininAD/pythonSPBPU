

#6

o = 0
i = int(input())
while i > 10:
    o = o + i%10
    i = i//10
o = o + i
print(o)
