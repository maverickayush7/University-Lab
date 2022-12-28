# 4.Write a program using callback mechanism to 
# (a) Sort the list based on the name and display.
# (b)Sort the list based on the total of P C M marks in descending order and display.


# a
s = [("890","ram",(95,78,99)),("123","kishan",(90,98,89)),("567","arjun",(59,68,100))]

def name(t):
    return t[1]
    
name = sorted(s, key = name)
print("Student list is sorted based on 2nd field, Name:\n", name)


# b
s = [("890","ram",(95,78,99)),("123","kishan",(90,98,89)),("567","arjun",(59,68,100))]

def totalmarks(t):
    return t[2][0]+t[2][1]+t[2][2]
    
name = sorted(s, key = totalmarks)
print("Student list is sorted based on totalmarks:\n", name)