def is_same(a,s,d,f,g,h):
    if a == f:
        if s == g:
            return True
        elif d == h:
            return True
        else:
            return False
    else:
        if s == g:
            if d == h:
                return True
            else:
                return False

n = int(input())
p =input().split(',')
q = []
for i in p:
    q.append(int(i))
for i in range(3, 3*n, 3):
    d=0
    if is_same(q[i-3],q[i-2],q[i-1],q[i+1],q[i+2],q[i+3]):
        d = q[i-3]+q[i-2]+q[i-1]-q[i+1]-q[i+2]-q[i+3]
        if d < 0:
            d = d * (-1)
        l
