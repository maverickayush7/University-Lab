#Given 3 sides of Triangle
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))
s=(a+b+c)/2.0
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle:",area)


#Given 2 sides and included an angle of Triangle
import math 
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the angle in degrees:"))
area=0.5*a*b*math.sin(c)
print("Area of the triangle:",area)

#Given 2 sides and a height of Triangle
import math
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
h=float(input("Enter the height:"))
c=h/a
area=0.5*a*b*math.sin(c)
print("Area of the triangle:",area)