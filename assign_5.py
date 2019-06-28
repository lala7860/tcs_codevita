def encrypt(text,key): 
    result = ""
    keys = []
    for x in range(len(key)):
        cha = key[x]
        if (cha.isupper()): 
            keys.append((ord(cha) - 65) % 26)
        else: 
            keys.append((ord(cha) - 97) % 26)
    for i in range(len(text)): 
        char = text[i]
        s = i%len(key)
        if(ord(char) > 47 and ord(char) < 58):
            result += chr((ord(char) + keys[s] - 48) % 10 + 48)
        elif (char.isupper()): 
            result += chr((ord(char) + keys[s] - 65) % 26 + 65)
        elif(char.islower()): 
            result += chr((ord(char) + keys[s] - 97) % 26 + 97)
        elif(ord(char) == 46 or ord(char) == 44 or ord(char) == 63 ):
            if ord(char) == 44:
                result += '.'
            elif ord(char) == 46:
                result += '?'
            else:
                result += ','   
        else:
            result += char
            print(ord(char))
    return result 

 
text = input("Enter a string: ")
key = (input("Enter key : " ))
print("Vigenere polyalphabetic cipher: " + encrypt(text,key) )