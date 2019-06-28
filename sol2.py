t = int(input())
while t:
    n = int(input())
    string, x = input().split()
    length = len(string)
    alist = []
    for i in range(length):
            for j in range(i,length):
                alist.append(string[i:j + 1])
    count=0
    for s in alist:
        if x in s:
            count+=1
    print(count)
    print(alist)
    t-=1