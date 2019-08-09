num = int(input("Enter a value "))
factorial = 1
if num < 0:
   print("invalid num")
elif num == 0:
   print("0 fact is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial is",factorial)