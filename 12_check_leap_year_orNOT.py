# check leap year or not

year =1968
#year=int(input("enter year :"))
if year % 400 == 0 and year % 100 == 0:
    print("this is leap year:",year)
elif year % 4 == 0 and year % 100 != 0:
    print("this is leap year",year)
else:
    print("not leap year")    