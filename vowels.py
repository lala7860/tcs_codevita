import math

def primes1(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

t = int(input())
while t:
    n = int(input())
    if n < 4:
        print(-1)
    else:
        a = math.floor(math.sqrt(n))
        lst2 = []
        lst = primes1(a+1)
        for x in lst:
            for i in lst:
                c = x ** i
                if c <= n:
                    lst2.append(c)
        print(lst2)
        print(max(lst2))
    t-=1
