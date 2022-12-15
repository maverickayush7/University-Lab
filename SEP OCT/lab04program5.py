'''y=int(input("Enter year: "))
m=int(input("Enter month(1-12): "))
d=int(input("Enter date(1-31): "))
import datetime
n=datetime.date(y,m,d)
print("Date you entered is: ",n)
if y>0 and 0<m<=12:
    if m in [4,6,9,11] and 0<d<=30:
        print("Valid Date")
    elif m in [1,3,5,7,8,10,12] and 0<d<=31:
        print("Valid Date")
    elif m==2 and y%4==0 and 0<d<=29:
        print("Valid Date")
    elif m==2 and y%4!=0 and 0<d<=28:
        print("Valid Date")
    else:
        print('ERROR!')
else:
    print("ERROR!")
import datetime
if m in [4,6,9,11]:
    if 0<d<30:
        D=d+1
        N=datetime.date(y,m,D)
        print("Next date is: ",N)
    elif d==30:
        D=1
        M=m+1
        N=datetime.date(y,M,D)
        print("Next date is: ",N)
    else:
        print("ERROR!")
elif m in [1,3,5,7,8,10]:
    if 0<d<31:
        D=d+1
        N=datetime.date(y,m,D)
        print("Next date is: ",N)
    elif d==31:
        D=1
        M=m+1
        N=datetime.date(y,M,D)
        print("Next date is: ",N)
    else:
        print("ERROR!")
elif m==12 and 0<d<31:
    D=d+1
    N=datetime.date(y,m,D)
    print("Next date is: ",N)
elif m==12 and d==31:
    D=1
    M=1
    Y=y+1
    N=datetime.date(Y,M,D)
    print("Next date is: ",N)
elif m==2 and y%100!=0 or y%400==0:
    if 0<d<29:
        D=d+1
        N=datetime.date(y,m,D)
        print("Next date is: ",N)
    elif d==29:
        D=1
        M=m+1
        N=datetime.date(y,M,D)
        print("Next date is: ",N)
    else:
        print("ERROR!")
elif m==2 and y%100!=0 or y%400==0:
    if 0<d<28:
        D=d+1
        N=datetime.date(y,m,D)
        print("Next date is: ",N)
    elif d==28:
        D=1
        M=m+1
        N=datetime.date(y,M,D)
        print("Next date is: ",N)
    else:
        print("ERROR!")
else:
    print("ERROR!")'''





y=int(input("Year:"))
m=int(input("Month:"))
d=int(input("Date:"))
if ((y%4==0 and (y%100!=0 or y%400==0)) and (m==2 and d==29)):
    m1=m+1
    d1=1
    print("Nextdate:",d1,m1,y)
elif(m==2 and d==28):
    m5=m+1
    d5=1
    print("Next date:",d5,m5,y)
elif(m==12 and d==31):
    y2=y+1
    m2=1
    d2=1
    print("Next date:",d2,m2,y2)
elif((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d==31):
    if(m==12 and d==31):
        y7=y+1
        m7=1
        d7=1
        print("Next date:",d7,m7,y7)
    else:
        m3=m+1
        d3=1
        print("Next date",d3,m3,y)
elif((m==4 or m==6 or m==9 or m==11) and d==30):
    m4=m+1
    d4=1
    print("Next date:",d4,m4,y)
elif((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==4 or m==6 or m==9 or m==11 or m==2 or m==12) and d<=27):
    d6=d+1
    print("Next date:",d6,m,y)
else:
    print("Date is Invalid")