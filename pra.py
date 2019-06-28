def encrypt(text,e, n): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()):
            a = ord(char)
            print((a**e)%n)
            result += chr(((a**e)%n))
        else: 
            a = ord(char) - 96
            result += chr(((a**e)%n)%26 + 96)
    return result

def decrypt(text,d, n): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()):
            a = ord(char)
            result += chr(((a**d)%n))
        else: 
            a = ord(char) - 96
            result += chr(((a**d)%n)%26 + 96)
    return result

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

text = "BD"
p = 173
q =149
e = 3
n = p*q
# d = 11
d = find_private(p, q, e)
print(d)
# print ("Text  : " + text )
s = encrypt(text, e, n)
print ("Encrypt: " + s)
# print ("Decrypt: " + decrypt(s, d, n))




    