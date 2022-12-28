'''3.	Write a function to mimic reduce - called myreduce. Test this with the following calls.
a)	Given a list of numbers, find maximum in the list.
b)	Given a list of integers, combine all integers to form a single integer. '''

#myreduce 
def myreduce(my_function, my_list):
    r = my_list[0]
    for next in my_list[1:]:
        r = my_function(r, next)
    return r


# 3 (a)

l = [23,45,12,47,54]
print( myreduce( lambda x , y : x if x > y else y, l))


# 3(b) 

l = [1,25,32,4]
print( int( myreduce( lambda x, y : str(x) + str(y), l)))
