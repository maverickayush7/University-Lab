
# 2. Write a program that takes a word from the user and counts the number of occurrences of that word in a file.

fn=input("enter file name:")
fo=open(fn,"r")
f=fo.read()
l=f.split()
word=input("enter the wpord which you want:")
count=0
for i in l:
    if i==word:
        count+=1
print(count)
