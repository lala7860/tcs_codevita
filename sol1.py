t=int(input())
for k in range(t):
    l=[0]*32
    arr=[]
    n=int(input())
    for z in range(n):
        s1 = list(set(input()))
        print(s1)
        numb = 0
        for cha in s1:
            if cha == 'a':
                numb = numb +10000
            elif cha == 'e':
                numb = numb+1000
            elif cha == 'i':
                numb =numb +100
            elif cha == 'o':
                numb =numb+10
            elif cha == 'u':
                numb=numb+1
        val=int(str(numb),base=2)
        print(val)
        arr.append(val)
        l[val]=l[val]+1
    print(l)
    c=0
    
    for i in range(1,31):
        for j in range(i+1,32):
            # print("i = ", i,"j=", j)
            if((l[i] and l[j]) and ((i | j) == 31)):
                print("i = ", i,"j=", j)
                print((i | j))
                c=c+l[i]*l[j]
        
    c=c+(l[31]*(l[31]-1))//2
    print(c)