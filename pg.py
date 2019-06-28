from itertools import combinations

def com(start, end, const):
    lst = []
    for x in range(start, end):
        lst.append(chr(64 + x))
    comb = combinations(lst, const)
    return list(comb)



a = []
for i in range(6):
    a.append(int(input()))
no = input().split(" ")
print(no)
once = input()

combination_x = com(1, a[0], a[1])
combination_y = com(a[0], a[2], a[3])
combination_z = com(a[2], a[4], a[5])
print(combination_x)


