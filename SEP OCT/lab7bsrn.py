#  2)Given a list : SRN, P_marks, C_marks, M_marks and B_marks.
#  1. Create a dict with SRN as the key and marks in P, C, M, B as a list.
#  2. Make another dict of srn and total marks and display in the order of marks.

'''n=int(input("total number of enteries you need :"))
l=[]
d={}
for i in range (1,n+1):'''

srn = [1,2,3]
Pmarks = [80, 89, 91]
Cmarks = [45, 85, 99]
Mmarks = [75, 86, 89]
Bmarks = [98, 48, 85]


#1
d1 = {}
for i in range(len(srn)):
    d1[srn[i]] = [Pmarks[i], Cmarks[i], Mmarks[i], Bmarks[i]]
print(d1)

#2
d2={}
for i in range(len(srn)):
    d2[srn[i]] = Pmarks[i] + Cmarks[i] + Mmarks[i] + Bmarks[i]



d2=sorted(d2.items())

print(dict(d2))