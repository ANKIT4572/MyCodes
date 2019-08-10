def fibonacci(n1,n2,count):
    num = int(input("enter the value"))

    if num <= 0:
        print("Please enter a positive integer")
    elif num == 1:
        print(n1)
    else:
        while count < num:
            print(n1)
            nth = n1 + n2

            n1 = n2  # update value
            n2 = nth
            count += 1
fibonacci(0,1,0)
