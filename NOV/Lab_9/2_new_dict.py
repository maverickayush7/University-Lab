'''2.	Given a dict where values are not unique, 
        write a function to create a new dict where the key is the value 
        and the value is concatenated keys of the original dict and return it. 

Input: {'apple':'fruit', 'cat':'mammal', 'beans':'veg', 'dog':'mammal', 'mango':'fruit'} 
Output: {'fruit':['apple', 'mango'], 'mammal':['cat', 'dog'], 'veg':['beans']} '''


gDict =  {'apple':'fruit', 'cat':'mammal', 'beans':'veg', 'dog':'mammal', 'mango':'fruit'} 
cDict = {}
for i in gDict:
    if gDict[i] in cDict: 
        cDict[gDict[i]].append(i)
    else: 
        cDict[gDict[i]] = [i]
print(cDict)