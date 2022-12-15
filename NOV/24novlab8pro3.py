# 3. Write a program to read a random line from a file.
import random

fn=input("enter file name :")
fo=open(fn,"r")
f=fo.readlines()
n=random.choice(f)

print(n)