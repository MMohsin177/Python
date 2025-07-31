#factorial(5!= 1*2*3*4*5)

# factorial  by using for loop
'''
num=int(input("enter a num :"))
factorial=1 #initializing with 1.We will multiply this by 1 × 2 × 3 ... × num in the loop later.
'''

#example

# Take input from user
num = int(input("Enter a number: "))

# Check for negative numbers
if num < 0:
    print("Factorial does not exist for negative numbers:", num)

# Handle the base case: 0! = 1
elif num == 0:
    print("Factorial of 0 is: 1")

# Handle positive numbers
else:
    factorial = 1  # Initialize before using
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is:", factorial)
  
    
"""
    Example: if num = 4:
factorial = 1
i = 1 → factorial = 1 × 1 = 1
i = 2 → factorial = 1 × 2 = 2
i = 3 → factorial = 2 × 3 = 6
i = 4 → factorial = 6 × 4 = 24

"""
    
# using recursion method(A function calls itself again and again until it reaches a base condition.)

def fact(a):
    if a < 0:
        return "Factorial of negative number doesn't exist"
    elif a == 0:  # 0! = 1
        return 1
    else:
        return a * fact(a - 1)

# Take input from user
num = int(input("Enter a number: "))
result = fact(num)

# Print the result
print("Factorial of", num, "is", result)


"""
return(a * fact(a -1))
 fact(a)
This is the current function call.

👉 fact(a - 1)
This is the recursive call — the function calls itself, but with a smaller number each time.

👉 a * fact(a - 1)
This multiplies the current number a with the result of the smaller factorial.

..............................................
✅ Sample Output:
If input is 5:

fact(5)
→ 5 * fact(4)
→ 5 * 4 * fact(3)
→ 5 * 4 * 3 * fact(2)
→ 5 * 4 * 3 * 2 * fact(1)
→ 5 * 4 * 3 * 2 * 1 * fact(0)
→ 5 * 4 * 3 * 2 * 1 * 1 = 120
"""