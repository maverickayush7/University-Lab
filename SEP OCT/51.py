'''Lab 5
Q1 Check whether a given number is
 (i) Perfect sqaure
 (ii) fibonacci Series
 (iii) perfect power of 2
Q2 Find the factors of a given number. Count the number of factors , Check Prime
Q3 Display the elements of a GP given a and r and max value
Q4 if n = 4
   1 + 2 + 3 + 4 = 10
   1*2 *3*4 =  24
Q5 if in input is 4
print 1 2 3 4
      8 7 6 5'''



#Q1(i)

import math
n = float(input("Enter N : "))
r = math.sqrt(n)
r = math.floor(r)
if (r**2 == n):
    print("Perfect Sqaure")
else:
    print("Not a Square")

#Q1)(ii)
#fibonacci series 
n=int(input("How many terms ?"))
n1,n2=0,1
count=0
if n<=0:
    print("Enter a positve integer")
elif n==1:
    print(n1)
else:
    print("Fibonacci Series is")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1



#Q1(iii)
n = int(input("Enter N :"))
i = 0
for i in range(n):
    if (2**i == n):
        print("Power of 2")
        break







