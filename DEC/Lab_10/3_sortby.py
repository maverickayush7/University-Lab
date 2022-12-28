# 3.Write a program using callback mechanism to 
# (a)Sort the given list based on name length and display.
# (b)Sort the given list based on last name and display.

# a
authors = ['Rabindranath Tagore', 'Khushwant Singh', 'Vikram Chandra', 'Mulk Raj Anand',
           'RK Narayan ', 'Jhumpa Lahiri']

print(sorted(authors, key=len)) #length-wise  


# b
authors = ['Rabindranath Tagore', 'Khushwant Singh', 'Vikram Chandra', 'Mulk Raj Anand',
           'RK Narayan ', 'Jhumpa Lahiri']

def lname(s):
    return s.split()[-1]

print(sorted(authors, key=lname))  #ordered alphabetically
