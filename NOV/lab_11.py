'''Programs on lambda functions and functional programming

1.	Write a Python program using lambda function.
a)	Multiply argument x with argument y and print the result.
b)	To find whether a given string starts with a given character.
c)	To extract year, month, day and time from datetime.
d)	To sort a list of dictionaries based on some key.

2.	Write a Python program using map/reduce/filter and lambda.
a)	Given a list of strings, remove all strings having first character as digit.
b)	Given a list of numbers, find maximum in the list.
c)	Given a list of tuples containing two integers, remove all tuples where second element in tuple is not a factor of first element.

3.	Write a function to mimic reduce - called myreduce. Test this with the following calls.
a)	Given a list of numbers, find maximum in the list.
b)	Given a list of integers, combine all integers to form a single integer. '''


#1 (a)
res=lambda x,y:x*y
print("multiplied : ", res(2,3))



#1 (b)

start_with = lambda x: True if x.startswith('I') else False
print(start_with("Irony"))

start_with = lambda x: True if x.startswith('X') else False
print(start_with("Ayush"))


#1 (c)
from datetime import datetime

# get current date
datetime_object = datetime.now()
print(datetime_object)
print(datetime_object.year)
print(datetime_object.month)
print(datetime_object.day)
a=lambda t : (datetime_object)


#1(d)
