#Find roots of a quadratic equation
print("Let the quadratic equation be ax^2+bx+c=0")
print("values of a,b,c:")
a=int(input("Value of a: "))
b=int(input("Value of b: "))
c=int(input("Value of c: "))
d=b**2-4*a*c
if d==0:
    root=-b/(2*a)
    print("Roots of the equation are ",root,root,sep=',')
elif d>0:
    root1=((-b)+d**0.5)/(2*a)
    root2=((-b)-d**0.5)/(2*a)
    print("Roots of the equation are ",root1,root2,sep=',')
else:
    print(d)