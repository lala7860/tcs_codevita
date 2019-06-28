t = int(input())
while t:
    n, d = input().split(" ")
    a = list(n)
    e=''
    a.append(d)
    for i in range(len(a)-1,0,-1):
        if a[i] < a[i-1]:
            a.pop(i-1)
            a.append(d)
        else:
            pass
    a.pop()
    for i in a:
        e+=i
    print(int(e))
    t-=1
