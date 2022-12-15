#Q4 if n = 4
#  1 + 2 + 3 + 4 = 10
#   1*2 *3*4 =  24

#Q4
n = int(input("Enter N :"))
i = 1
sum = 0
pro = 1
for i in range(1,n+1):
    sum = sum + i
    pro = pro*i
print(sum)
print(pro)

