#Program 
'''1)Program to sort given list of elements(both ascending and descending).
2)Program to remove all occurrences of a number entered by the user in the given list.
3)Program to find the addition of two matrices.
4)Given a hetereogenous list,create separate lists for differentr types of data.
5)Program to print identity matrix using list
6)Program to generate a pascal's triangle.'''


#1)
'''lst=eval(input("Enter the list: "))
print(lst)
lst1=sorted(lst)
lst2=lst1[::-1]
print(lst1)]
print(lst2)'''

#2)
'''lst=eval(input("Enter list: "))
num=int(input("Enter the number to be removed: "))
lst1=[]
for i in lst:
    if i!=num:
        lst1.append(i)
print(lst1)'''

#3)
'''print("Enter a 3x3 matrix")
lst1=list(map(int,input("Enter first row of matrix: ").split()))
lst2=list(map(int,input("Enter first row of matrix: ").split()))
lst3=list(map(int,input("Enter first row of matrix: ").split()))
for i in range(len(lst1)):
    lst1[i]+=1
for i in range(len(lst2)):
    lst2[i]+=1
for i in range(len(lst3)):
    lst3[i]+=1
print(lst1)
print(lst2)
print(lst3)'''

#4)
'''lst=eval(input("Enter list: "))
#int float string bool
lst1=[]
lst2=[]
lst3=[]
lst4=[]
for i in lst:
    if type(i)==int:
        lst1.append(i)
    elif type(i)==float:
        lst2.append(i)
    elif type(i)==str:
        lst3.append(i)
    else:
        lst4.append(i)
print(lst1)
print(lst2)
print(lst3)
print(lst4)'''

#5)
'''n=int(input("Enter the dimension of matrix: "))
for i in range(0,n):
    for j in range(0,n):
        if i==j :
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()'''