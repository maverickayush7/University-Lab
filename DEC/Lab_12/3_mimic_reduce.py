#3.Write a function to mimic reduce - called myreduce. Test this with the following.
#     a) Given a multiword name, print its first letters
#     b) Find the sum of first n natural numbers
#     c) Find factorial of n

# 3(a)
def capital_word(s1,s2):
    return s1+s2[0]    

def myreduce(my_function, my_list):
    result=''
    for name in my_list:
        result=my_function(result,name)
    return result

name_list=['Ayush','Aditya','Kumar']
print(myreduce(capital_word,name_list))



# 3(b) Find the sum of first n natural numbers
def add2(n1,n2):
    return n1+n2

def myreduce(my_function, my_list):
    result=0
    for num in my_list:
        result=my_function(result,num)
    return result

n=10
print(f'The sum of first {n} natural numbers is', end=' ')
print(myreduce(add2,range(1,n+1)))   



#3(c) Find factorial of n
def prod2(n1,n2):
    return n1*n2

def myreduce(my_function, my_list):
    result=1
    for num in my_list:
        result=my_function(result,num)
    return result

n=5
print(f'The factorial of {n} is', end=' ')
print(myreduce(prod2,range(2,n+1)))     

