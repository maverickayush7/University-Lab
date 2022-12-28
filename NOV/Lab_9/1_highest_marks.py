#Lab 9 - Programs on functions.

'''1.	Given two lists as arguments (marks and names), write a function to return a tuple containing the highest marks and the corresponding name. 
Input:  marks = [90, 70, 95, 60]    names = ['Raj', 'Sita', 'Ram', 'Ganga']
Output: (95, 'Ram')'''

def getHighestMarks(marks, names):
    m = max(marks)
    i = marks.index(m)
    mName = names[i]
    return m, mName


marks = [90, 70, 95, 60]
names = ['Raj', 'Sita', 'Ram', 'Ganga']

print(getHighestMarks(marks, names))
