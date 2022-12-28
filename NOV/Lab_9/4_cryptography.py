'''4.	Write function to code(or encrypt) a given string s1 and write an another function to decode(or decrypt) the coded string.
    * Encryption strategy_1: change a to z, b to y ... z to a, y to b 
    * Encryption strategy_2: change a to b, b to c, .... and z to a'''

def encrypt(s):
    for i in range(len(s)):
        s[i] = chr(ord(s[i]) + 1) 

def decrypt(s):
    for i in range(len(s)):
        s[i] = chr(ord(s[i]) - 1) 


s = "hello ayush"
s = list(s)
encrypt(s)

print("Encrypted:", ''.join(s))
decrypt(s)
print("Decrypted:", ''.join(s))