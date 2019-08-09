num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    sum = sum * 10 + temp % 10
    temp = temp/10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")