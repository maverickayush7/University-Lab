#Age calculator

print("Please enter your Birthday")
bdy=int(input("Year   :"))
bdm=int(input("Month(1-12):"))
bdd=int(input("Date(1-31):"))

import datetime

birthdate=datetime.date(bdy,bdm,bdd)
print("Your birth date:",birthdate)

todaydate=datetime.datetime.today().date()
print("Today's date:",todaydate)

numdays=(todaydate-birthdate).days
print("Your age in days:",numdays)


seconds=numdays*86400
print("Your age in seconds:",seconds)

day=datetime.datetime(1947,8,15).weekday()
print("India became independent on day",day)

beginyd=datetime.date(2022,1,1)
#todaydate=datetime.datetime.today().date()

print(beginyd)
print(todaydate)
print("No. of days=",(todaydate-beginyd).days)

