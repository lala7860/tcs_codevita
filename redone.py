t = int(input())
while t:
    n = int(input())
    l = []
    for x in range(1, n+1):
        l.append(x)
    for i in range(1, n):
        print(l)
        x=l.pop(0)
        y = l.pop()
        z = x + y + x*y
        l.append(z)
    c = l.pop()
    c = c%1000000007
    print(c)
    t-=1   