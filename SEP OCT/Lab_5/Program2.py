#Q2 Find the factors of a given number. Count the number of factors , Check Prime

n = int(input("Enter N :"))
i = 1
fac = []
for i in range(1,n+1):
    if (n%i == 0):
        fac.append(i)
print(fac)
print(len(fac))
if (len(fac) >2 ):
    print("Not a prime")
else:
    print("Prime")