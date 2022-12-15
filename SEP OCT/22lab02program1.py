basic=25000
a=int(input("Enter Total no. of camera sold:"))
b=int(input("Enter Total price of camera sold:"))
bonus=a*200
commission=b*12/100
salary=basic+bonus+commission
print("Salary:",salary)