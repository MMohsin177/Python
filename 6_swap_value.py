# by third variable

x=12
y=13

temp=x # temp=12
x=y  #x=13
print(f'x become',x)
y=temp #temp is 12 so y =12
print(f'y become ',y)

print(f'now value of x and y after swap is :{x},{y} ')


# without third variable
a=5
b=6
a,b=b,a
print(f'value of a is {a} and  value of b is {b}')