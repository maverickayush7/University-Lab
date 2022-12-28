#Q3 Display the elements of a GP given a and r and max value

a = int(input("Enter a first number"))
r = int(input("The common ratio"))
m = int(input("Enter the max value"))
i = 1
n = 0
while i>=0 :
    if a*(r**(i-1)) == m:
        n = i
        break
    i = i+1
print(n)
i = 1
l =[]
for i in range(0,n):
    p = a*(r**(i))
    l.append(p)
print(l)
print(sum.p)