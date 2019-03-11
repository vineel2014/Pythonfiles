import calendar

print("******Monthly Calendar************")
x=int(input("Enter four digit calendar year"))
y=int(input("Enter calender month number"))


cal=calendar.month(x,y)

print(cal)
