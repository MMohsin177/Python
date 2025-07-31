# quardic equation ax^2 + bx = c
# a,b,c are real num( 2,3,5)
# a != 0

a=int(input("enter a num( a!= 0):"))
b=int(input("enter a num    :"))
c=int(input("enter a num   :"))

# quardic formula:  x= ((-b) +- (b^2 - 4ac)^1/2 )  / 2a

import cmath                  # cmath = for both real or imaginary problem
# first find  discriminant 
D=(b**2)-(4*a*c)  # b^2 - 4ac
print("Discrimant IS",D)
root1=(-b - cmath.sqrt(b**2 - 4*a*c))  # root1 for - sign 
root2=(-b + cmath.sqrt(D))  #root2  for + sign
print(f'the roots are {root1}  and {root2}')