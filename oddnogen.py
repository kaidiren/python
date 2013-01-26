from random import randint

def odd(n):
    if n%2==0:
        return 1
    else:
        return 0

allnums=[]

for eachnum in range(9):
    allnums.append(randint(1,99))
print allnums
print filter(odd,allnums)
