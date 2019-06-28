t = int(input())
while t:

    f, s1, s2 = [int(x) for x in input().split()]
    q = int(input())

    for x in range(q):
        flag = 1
        c1, c2 = [int(i) for i in input().split()]
        if c1:
            flag = flag*(-1)
        if c2:
            flag = flag*(-1)
        if flag == 1:
            if f == 1:
                print("ON")
            else:
                print("OFF")
        else:
            if f == 0:
                print("ON")
            else:
                print("OFF")
    t-=1
