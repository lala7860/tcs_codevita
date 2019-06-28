import math
import sys


N = int(input())
if N > pow(10, 5):
    sys.exit()
A = []
B = []

A = input().split(" ")
if len(A) > N:
    sys.exit()
for i in A:
    if int(i) > pow(10, 5):
        sys.exit()
    B.append(int(i))
Q = int(input())
H = [0]*Q
print(H)
for x in range(Q):
    
    D = []
    D = input().split(" ")
    E = []
    for x in D:
        E.append(int(x))
    H[x] = 1
    for i in range(E[0], E[1]+1):
        c = B[i-1]
        c = math.factorial(c)%1000000007
        H[x] = H[x] * c
    H[x] = H[x]%1000000007
    H[x] = pow(H[x], (E[1]-E[0]))
    H[x] = H[x]%1000000007
    Q = Q-1

for x in H:
    print(x)
    