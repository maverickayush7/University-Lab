'''Week 10: Lab 9- Problem Statements
Programs on functions.


1.	Given two lists as arguments (marks and names), write a function to return a tuple containing the highest marks and the corresponding name. 
Input:  marks = [90, 70, 95, 60]    names = ['Raj', 'Sita', 'Ram', 'Ganga']
Output: (95, 'Ram') 
2.	Given a dict where values are not unique, write a function to create a new dict where the key is the value and the value is concatenated keys of the original dict and return it. 

Input: {'apple':'fruit', 'cat':'mammal', 'beans':'veg', 'dog':'mammal', 'mango':'fruit'} 
Output: {'fruit':['apple', 'mango'], 'mammal':['cat', 'dog'], 'veg':['beans']} 


3.	Write function definitions for the given function headers with null statement to solve the below problems.
def is_square(x): pass 
	def is_even(x): pass
a.	Check whether a given number is a perfect square.
b.	Find all numbers between 1 and n which are: 
i.	 both square and even 
ii.	both even and not square 


4.	Write function to code(or encrypt) a given string s1 and write an another function to decode(or decrypt) the coded string.
    * Encryption strategy_1: change a to z, b to y ... z to a, y to b 
    * Encryption strategy_2: change a to b, b to c, .... and z to a



5.	Display
a.	Identity matrix for a given matrix of order n.
b.	Triangular matrix (both lower and upper) for a given matrix.'''



'''#1  
def getHighestMarks(marks, names):
    m = max(marks)
    i = marks.index(m)
    mName = names[i]
    return m, mName


marks = [90, 70, 95, 60]
names = ['Raj', 'Sita', 'Ram', 'Ganga']

print(getHighestMarks(marks, names))


'''

'''#2
gDict =  {'apple':'fruit', 'cat':'mammal', 'beans':'veg', 'dog':'mammal', 'mango':'fruit'} 
cDict = {}
for i in gDict:
    if gDict[i] in cDict: cDict[gDict[i]].append(i)
    else: cDict[gDict[i]] = [i]
print(cDict)'''



'''#3
import math


def is_square(x): return math.sqrt(x) % 1 == 0
def is_even(x): return x % 2 == 0


#a 
n = int(input('n: '))
print("perfect sqare") if is_square(n) else print("not perfect square")


#b
n = int(input('n: '))
se = []
ens = []

for i in range(1, n+1):
    if is_even(i):
        if is_square(i): se.append(i)
        else: ens.append(i)

print("square and even: ", se)
print("even and not square: ", ens)'''
'''
#4
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
print("Decrypted:", ''.join(s))'''



#5
o = int(input("order: "))

for i in range(o):
    for j in range(o):
        if i == j: print('1', end = ' ')
        else: print('0', end = ' ')
    print()


#b
gMatrix = eval(input("Enter matrix as nested list: "))

# upper matrix
for i in range(len(gMatrix)):
    for j in range(len(gMatrix[i])):
        if i <= j: print(gMatrix[i][j], end = ' ')
        else: print('0', end = ' ')
    print()

print('\n\n')

# lower matrix
for i in range(len(gMatrix)):
    for j in range(len(gMatrix[i])):
        if i >= j: print(gMatrix[i][j], end = ' ')
        else: print('0', end = ' ')
    print()
print('\n\n')