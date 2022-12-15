#given 3 sides , check wheather a triangle is formed . If yes , find the area

print("Enter the values of sides of triangle:")
a=int(input("Side 1:"))
b=int(input("Side 2:"))
c=int(input("Side 3:"))
if a<b+c and b<a+c and c<a+b:
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("This triangle exists and its area is ", area)
else:
    print("This triangle does not exist")
