# 5) Flatten tuple of lists to Tuple

gt=eval(input("Enter:"))
l=[]
for i in gt:
    if type(i) is list:
        for j in i :
            l.append(j)
    else: l.append(i)
print(tuple(l))