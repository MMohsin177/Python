# check prime num in interval (beween two values)

lower=int(input("enter a lower limit:"))
upper=int(input("enter a upper limit:"))


for num in range(lower,upper+1):
    if num > 1: # Skip 0 and 1
        for i in range(2,num):
            if num % i==0:
                break  # Not prime, so exit inner loop
        else:
            print(num)

