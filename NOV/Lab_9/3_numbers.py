'''3.	Write function definitions for the given function headers with null statement to solve the below problems.
def is_square(x): pass 
	def is_even(x): pass
a.	Check whether a given number is a perfect square.
b.	Find all numbers between 1 and n which are: 
i.	 both square and even 
ii.	both even and not square '''


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
        if is_square(i):
            se.append(i)
        else: 
            ens.append(i)

print("square and even: ", se)
print("even and not square: ", ens)