# 4) Repeated in Tuples

t=eval(input("Enter:"))
s=set()
for i in t :
    if t.count(i)>1 :
        s.add(i)
        print(s)
