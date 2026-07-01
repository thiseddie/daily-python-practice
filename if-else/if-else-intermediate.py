#1. largest of three number.

a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = int(input("enter the third number :"))

if a >= b and b >=c :
    print("the first number is the largest")
elif b>=a and a>=c:
    print("the second number entered is the largest")
else:
    print("the third number is the largest")
