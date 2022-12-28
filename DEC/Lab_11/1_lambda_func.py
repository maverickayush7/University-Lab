'''Programs on lambda functions and functional programming

1.	Write a Python program using lambda function.
a)	Multiply argument x with argument y and print the result.
b)	To find whether a given string starts with a given character.
c)	To extract year, month, day and time from datetime.
d)	To sort a list of dictionaries based on some key.'''


# 1(a)
res=lambda x,y:x*y
print("multiplied : ", res(2,3))



# 1(b)

start_with = lambda x: True if x.startswith('I') else False
print(start_with("Irony"))

start_with = lambda x: True if x.startswith('X') else False
print(start_with("Ayush"))


# 1(c) To extract year, month, day and time from datetime.
import datetime

DT=datetime.datetime.now()

print('---------------------')
date_fn=lambda date : date.date()
day_fn=lambda date : date.day
month_fn=lambda date : date.month
year_fn=lambda date : date.year
print('Todays Date :',date_fn(DT))
print('Day  :',day_fn(DT))
print('Month:',month_fn(DT))
print('Year :',year_fn(DT))

print('---------------------')
time_fn=lambda t : t.time()
hour_fn=lambda t : t.hour
mins_fn=lambda t : t.minute
secs_fn=lambda t : t.second
print('Time Now :',time_fn(DT))
print('Hour :',hour_fn(DT))
print('Mins :',mins_fn(DT))
print('Secs :',secs_fn(DT))



# 1(d) To sort a list of dictionaries based on some key

models = [{'make':'Apple', 'model':69, 'color':'Black'}, 
          {'make':'Redmi', 'model':'35', 'color':'Gold'}, 
          {'make':'Poco', 'model':23, 'color':'Pink'}]
print("Original list of dictionaries :")
print(models)

sorted_models = sorted(models, key = lambda d: d['color'])
print("Sorted List of dictionaries :")
print(sorted_models)
