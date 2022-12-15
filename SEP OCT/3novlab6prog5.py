#program to print identity matrix using list 
'''n=int(input("Enter the dimension of matrix: "))
for i in range(0,n):
    for j in range(0,n):
        if i==j :
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
        print()'''


def Identity(size):
    for row in range(0, size):
        for col in range(0, size):
 
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
 
# Driver Code       
size = 5
Identity(size)