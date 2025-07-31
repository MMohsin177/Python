#fibonacci sequence

"""
🧠 What is Fibonacci Sequence?
The Fibonacci sequence is a series of numbers in which each number
is the sum of the two preceding ones, starting from 0 and 1.

💡 Example Breakdown:

Term(n)	  Fibonacci Number	   How It Was Calculated
0	           0	                (Starting value)
1	           1                 	(Starting value)
2	        0 + 1 = 1	       Previous two terms: 0 and 1
3	        1 + 1 = 2	       Previous two terms: 1 and 1
4        	1 + 2 = 3	       Previous two terms: 1 and 2
5	        2 + 3 = 5	       Previous two terms: 2 and 3"""

a=0
b=1
num=int(input("enter num for fibonacci sequence:"))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c= a+b
        a=b
        b=c
        print(c)
