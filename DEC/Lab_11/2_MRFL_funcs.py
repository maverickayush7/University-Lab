'''2.	Write a Python program using map/reduce/filter and lambda.
a)	Given a list of strings, remove all strings having first character as digit.
b)	Given a list of numbers, find maximum in the list.
c)	Given a list of tuples containing two integers, remove all tuples where second element in tuple is not a factor of first element.
'''


# 2(a)
l=['2aditya','India','5Ayush','Argentina','1madam','hi']
print(list(filter(lambda x : False if x[0].isdigit() else True,l)))


# 2(b) 
from functools import reduce
num_list=[23,45,12,47,54]

print(reduce(lambda x,y:x if x>y else y, num_list))


# 2(c) Given a list of tuples containing two integers, 
#      remove all tuples where second element in tuple is not a factor of first element.

lst=[(2, 3), (4, 2), (6, 3), (6, 4), (32, 4), (64,8)]
print(list(filter(lambda x : True if x[0] % x[1] == 0 else False,lst)))