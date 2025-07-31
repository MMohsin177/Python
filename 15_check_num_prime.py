# prime num 2,3,5,7,11,13... (0,1 not prime or num%2 ==0 not prime)

num=int(input("enter a num :"))
if num <=1: # num=o,1 (not prime )
    print("not a prime num:",num)
else: 
    for i in range(2,num):# range i= 2,3,4,5,6
        if num % i ==0 :
            print("not a prime num:",num)
            break # if reminder is given 0 so num is not prime condition stop or show output
        else:
            print("its a prime num:",num) 