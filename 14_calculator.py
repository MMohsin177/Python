num1 = float(input("enter 1st num:"))
num2 = float(input("enter 2nd num :"))

choice = input("select operation : + ,- , * , /, // ,**,%   : ")

if choice == '+':
    print(f'Addition:' ,{num1 + num2})
elif choice == '-' :
    print(f'sutraction:',{num1 - num2})
elif choice == '*' :
    print(f'Multiplication:',{num1 * num2})    
elif choice == '/' :
    print(f'Division (float) :',{num1 / num2})
elif choice == '//' :
    print(f'Division (integer):',{num1 // num2})
elif choice == '**' :
    print(f'Exponent (power):',{num1 ** num2})
elif choice == '%' :
    print(f'Modulus (reminder):',{num1 % num2})
print("your calculation is end ")                    