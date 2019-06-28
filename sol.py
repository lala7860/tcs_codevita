t = int(input())
while t:
    b = int(input())
    c = b//10
    a = b%10
    if a>0:
        c+=1
    else:
        pass
    c*=10
    if c%1000 == 0:
        c+=10
    elif c%100 == 0:
        c+=10
    print(c)
    t-=1
    