#2.Write a function to mimic filter - called myfilter. Test this with the following.
#     a) Given a list of strings, remove all strings having first character as digit.
#     b) Pickup all words whose length exceeds 6.
#     c) Find all strings in a given line of text ending with a given suffix.


#2(a) Given a list of strings, remove all strings having first character as digit.

def myfilter(my_function, my_list):
    result = []
    for ele in my_list:
        if my_function(ele):
            result.append(ele)
    return result

str_list=['2aditya','India','5Ayush','Argentina','1madam']
print(myfilter(lambda s: not s[0].isdigit(), str_list))


#2(b) Pickup all words whose length exceeds 6.

'''def myfilter(my_function, my_list):
    result = []
    for ele in my_list:
        if my_function(ele):
            result.append(ele)
    return result'''

city_list=['Bangalore','Mysore','France','Electroniccity','Argentina']
print(myfilter(lambda s: len(s)>6,city_list))


#2(c) Find all strings in a given line of text ending with a given suffix.

def ends_with(word):
    return word.endswith(suffix)

'''def myfilter(my_function, my_list):
    result = []
    for ele in my_list:
        if my_function(ele):
            result.append(ele)
    return result
'''
words_list=input('Enter a line of text: ').split()
print(words_list)
suffix=input('Enter a suffix:')
print(myfilter(ends_with,words_list))

