import math
import sys

def get_remainder(num, divisor):
    return (num - divisor * (num // divisor))


N = int(input())
if N > pow(10, 5):
    sys.exit()

B = []

B = [int(x) for x in input().split(" ")]
if len(A) > N:
    sys.exit()
for i in A:
    if int(i) > pow(10, 5):
        sys.exit()
    B.append(int(i))
Q = int(input())
result = []
for x in range(Q):
    E = [int(x) for x in input().split(" ")]
    for x in D:
        E.append(int(x))
    H = 1
    for i in range(E[0], E[1]+1):
        c = B[i-1]
        c = math.factorial(c)
        c = get_remainder(c, 1000000007)
        H = H * c
    H = get_remainder(H, 1000000007)
    H = pow(H, (E[1]-E[0]))
    H = get_remainder(H, 1000000007)
    result.append(H)
    Q = Q-1
    
    
for x in result:
  	print(x)
    