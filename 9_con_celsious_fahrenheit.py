# convert celsious to fahrenheit 
#  F = (C× 9/5)+32


celsious=float(input("enter celsious temp:"))
fahrenheit=( celsious * 9/5)+32
print(f'{celsious} C temperature in  fahrenheit is :{fahrenheit}F')


# convert fahrenheit to celsious

#  C = (F - 32) * 5/9
 
fahrenheit=float(input("enter farhenheit temp:"))
celsious=( fahrenheit -32 )*5/9
print(f'{fahrenheit} F temperature in  celsious is :{celsious}C')