#Q5 if in input is 4
#print 1 2 3 4
#      8 7 6 5'''

n = int(input("Enter N :"))
i =1
for i in range(1,n+1):
    print(i,end=" ")
print()
i = 1
for i in range(0,n):
    print(2*n-i,end=" ")