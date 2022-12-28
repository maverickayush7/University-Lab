# 4. Write a program that takes a file name from the user and reads the contents(ie, lines) of the file in reverse order(ie, from bottom).

fn=input("enter the file name :")

fo=open(fn,"r")
f=fo.readlines()

n=len(f)
for i in range (n-1,-1,-1):
    print(f[i].strip())
