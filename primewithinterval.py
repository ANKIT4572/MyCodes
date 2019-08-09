lower = int(input("enter the lower num"))
upper = int(input("enter the upper num"))



for num in range(lower,upper+1):
    if num>0:
        for i in range(2, num):
            if (num % i) == 0:


                break

        else:
            print(num)






