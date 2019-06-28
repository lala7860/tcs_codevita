def check(arr1, arr2):
    l = len(arr1)
    score = 0
    for i in range(l):
        if arr1[i] == arr2[i]:
            score = score + 1
        else:
            pass
    return score

def campare(arr1, arr2):
    l = len(arr1)
    score = []
    for i in range(l):
        if arr1[i] <= arr2[i]:
            result3.append(arr1[i])
        else:
           result3.append(arr2[i])
    return result3

N = int(input())
M = int(input())
part = []
for x in range(M + 1):
    part.append([int(x) for x in input().split(" ")])

result = []
result1 = []
result3= []
for x in range(M):
    latest_key = part[x]
    result.append(check(latest_key, part[x+1]))
final_key = campare(part[-1], part[-2])
for x in range(M):
    result1.append(check(final_key, part[x]))

    

for x in result:
    print(x)
c = 0
d = 0
for i in range(M):
    if(c < result1[i]):
        c = result1[i]
        d = i
    else:
        pass
print(d+1, c)




