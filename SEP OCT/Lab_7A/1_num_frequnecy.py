# Lab-7 Program oN TUPLES

# 1) Program to find frequency of largest number

l=eval(input("List :"))
print(l.count(max(l)))


List = [11, 22, 88, 53, 88, 53, 88] 
largest = max(List) #using built-in function max
max_count = List.count(largest)
print("The frequncy of largest number", largest,"is",max_count) 
