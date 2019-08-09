num = int(input("enter the number"))


if num>0:
    for i in range(2, num):
        if (num%i)==0:
            print("not prime", num)
            print(i, "times", num // i, "is", num)
            break
    else:
        print("num is prime",num)

else:
    print("num is not prime",num)




