import bisect
nos = int(pow(10**11, 0.5))+1

primes = [True]*nos
primes[0] = primes[1] = False
pr = []
for ind, val in enumerate(primes):
    if val:
        pr.append(ind)
        for i in range(ind, nos, ind):
            primes[i] = False

exp = []
for i in range(len(pr)):
    for j in range(len(pr)):
        temp = pr[i]**pr[j]
        if temp<=10**11:
            exp.append(temp)
        else: break
exp.sort()

t = int(input())
while t:
    n = int(input())
    if n < 4:
        print(-1)
    elif n < 8:
        print(4)
    else:
        pos = bisect.bisect(exp, n)
        if pos == len(exp):
            print(-1)
        elif exp[pos] == n:
            print(exp[pos])
        else:
            print(exp[pos-1])
    t-=1
