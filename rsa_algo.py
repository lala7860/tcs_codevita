def find_private(p, q, e):
    n = p*q
    w = (p-1)*(q-1)
    a = [1, 0]
    b = [0, 1]
    d = [w, e]
    pri = 0
    k = 0
    while(d[-1] != 1):
        k = d[-2]//d[-1]
        a.append(a[-2]-(a[-1]*k))
        b.append(b[-2]-(b[-1]*k))
        d.append(d[-2]-(d[-1]*k))
    pri = b[-1]
    if pri > w:
        pri = pri % w
    elif pri < 0:
        pri = pri + w
    return pri
def give_num(st):
    a = ord(st)
    if a == 32:
        a = 0
    else:
        a -= 64
    return a

def spli_text(text):
    result=[]
    a=''
    for x in range(len(text)):
        a += text[x]
        if len(text) < 3:
            result.append(a)
        elif x%3 == 2:
            result.append(a)
            a=''
    return result

def message(array):
    result = []
    for x in array:
        a = 0
        l = len(x)
        for i in range(l):
            a += (give_num(x[i]))*27**(l-i-1)
        result.append(a)
    return result

def cipher_text(message, e, n):
    result = []
    for x in message:
        c = (x**e)**n
        result.append(c)
    return result


def plane_text(message, d, n):
    result = []
    for x in message:
        c = (x**d)**n
        result.append(c)
    return result




text = "ATTACK AT SEVEN"
t = spli_text(text)
m = message(text)
p = 173
q =149
e = 3
n = p*q
d = find_private(p, q, e)
c = cipher_text(m, e, n)
p = plane_text(c, d, n)
print(c)
