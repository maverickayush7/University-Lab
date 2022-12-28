#3 program to find the addition of two matrices

print("Enter a 3x3 matrix")
lst1=list(map(int,input("Enter first row of matrix:").split()))
lst2=list(map(int,input("Enter second row of matrix:").split()))
lst3=list(map(int,input("Enter third row of matrix:").split()))

for i in range (len(lst1)):
    lst1[i]+=1
for i in range (len(lst2)):
    lst2[i]+=1
for i in range (len(lst3)):
    lst3[i]+=1

print(lst1)
print(lst2)
print(lst3)