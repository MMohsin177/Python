num1=int(input("enter a 1st num:"))
num2=int(input("enter a 2nd num:"))
num3=int(input("enter a 3rd num:"))

if num1 > num2 and num1 > num3:
    print(" 1st num is largest",num1)
elif num2> num1 and num2 >num3:
    print(" 2nd num is largest",num2)
else:
    print("3rd num is largest",num3)   