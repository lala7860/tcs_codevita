t = int(input())
while t :
    x, y = [int(x) for x in input().split()]
    if x <= y:
        print(0)
    else:
        print(x-y)
    t-=1
