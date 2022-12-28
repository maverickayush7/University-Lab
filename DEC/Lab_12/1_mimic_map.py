# Lab 12  Programs on functional programming

# 1) Write a function mymap which takes a callable and an iterable,
#    creates a list,applies the callback to each element of the iterable
#    and puts the result into list and returns the list. mymap should mimic map.

# Test this with the following calls.
#     a) Create a list of squares of odd numbers from 1 to n.
#     b) Given a list of words, return a list of words with ing appended to it.
#     c) Given a list of words, return a list of tuples having the word and its length.



# 1(a)
def mymap(my_function, my_list):
    output_list=[]
    for ele in my_list:
        output_list.append(my_function(ele))
    return output_list
    
n = int(input("Enter value : "))
l= mymap(lambda n: n**2, range(1, n+1, 2))
print(l)



# 1(b)
def mymap(my_function, my_list):
    output_list=[]
    for word in my_list:
        output_list.append(my_function(word))
    return output_list
    
words_list=['study','work','help','bath','walk']
l=mymap(lambda word: word+'ing', words_list)
print(l)



# 1(c) Given a list of words, return a list of tuples having the word and its length.
def mymap(my_function, my_list):
    output_list=[]
    for word in my_list:
        output_list.append(my_function(word))
    return output_list
    
city_list=['Bangalore','Mysore','France','Electroniccity','Argentina']
l= mymap(lambda word: (word,len(word)) , city_list)
print(l)
