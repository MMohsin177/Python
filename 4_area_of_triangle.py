# area formula is = 1/2 * base * height

height=float(input("enter a num:"))
base= float(input("enter a num :"))
area_of_triangle= (1/2) * height *base
print("Area of a triangle is:",area_of_triangle)


# area of rectangle
area_of_rectangle=  height *base     # base=length
print("Area of a triangle is:",area_of_rectangle)


# area of circle       use module math because we need pi
import math
radius=5
area_of_circle=math.pi * radius **2     # pi * r^2
print("Area of a circle is:",area_of_circle)