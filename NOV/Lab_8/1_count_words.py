#24 November
# 1. Write a program that takes the file name from the user and counts the number of words in that file.

fn=input("enter file name :")
fo=open(fn,"r")
f=fo.read()
l=f.split()
print(len(l))
