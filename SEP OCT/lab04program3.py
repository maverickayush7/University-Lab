'''# given 4 side sand two diagonals of a quadrilateral , classify the quadrilateral as square , rhombus, rectangle and parallellogram.
import math
s1=float(input("Length of side One: "))
s2=float(input("Length of side Two: "))
s3=float(input("Length of side Three: "))
s4=float(input("Length of side Four: "))
d1=math.sqrt(s1*s2+s3*s4)
d2=math.sqrt(s1*s2+s3*s4)

if s1==s2==s3==s4:
    if d1==d2:
        print("The Quadrilateral is a Square.")
    else:
        print("The Quadrilateral is a Rhombus.")
elif s1==s3 and s2==s4 and s1!=s2 or s1==s2 and s3==s4 and s1!=s3 or s1==s4 and s2==s3 and s1!=s2:
    if d1==d2:
        print("The Quadrilateral is a Rectangle.")
    else:
        print("The Quadrilateral is a Parallelogram.")
else:
    print("NA")'''


a=float(input("Enter side AB: "))
b=float(input("Enter side BC: "))
c=float(input("Enter side CD: "))
d=float(input("Enter side AD: "))
d1=float(input("Enter diagonal 1:"))
d2=float(input("Enter diagonal 2:"))
if a==b==c==d:
    if d1==d2:
        print("Square")
    else:
        print("rhombus")
else:
    if d1==d2:
        print("Rectangle")
    else:
        print("Parallelogram")