n=int(input(("Enter 4-digit number:")))
d=n%10
n=n//10
c=n%10
n=n//10
b=n%10
n=n//10
a=n%10
n=n//10
print(a,b,c,d)
sum=a+b+c+d
print("Sum of individual numbers:",sum)