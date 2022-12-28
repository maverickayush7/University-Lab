#2 program to remove all occurance of a number entered by the user in the given list 

a=int(input("number of elements you want to enter in the list :"))
lt=[]
for i in range (0,a):
    b=int(input("enter a number :"))
    lt.append(b)
print(lt)
lt1=[]
c=int(input("which number you want to remove:"))
for i in lt:
    if c!=i:
        lt1.append(i)
print(lt1)