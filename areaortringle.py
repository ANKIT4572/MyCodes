a = float(input("enter the 1st side"))
b = float(input("enter thr 2nd side"))
c = float(input("enter thr 3nd side"))


#find semi peremetter
s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c))**0.5    #exponentional ** meaning
print("are of the tringle %0.2f",area)



