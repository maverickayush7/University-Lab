#1 program to sort given list of elements (both ascending and descending)
a=int(input("number of elements you want to enter in the list :"))
list=[]
for i in range (0,a):
    b=int(input("enter a number :"))
    list.append(b)
print(list)
n=list.sort()
print("sorted in ascending order :",list)
n=list.sort(reverse=True)
print("sorted in descending order :",list)




