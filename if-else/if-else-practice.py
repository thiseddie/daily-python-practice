#1. even odd


nums=int(input("enter the number:"))

if  nums % 2 ==0:
    print("even")
else:
    print("odd")


#2. positive negative or zero 

nums = int(input("enter the number:"))

if nums >0 :
    print("the entered number is positive")
elif nums <0 :
    print("the number entered is zero")
else:
    print("the number entered is zero")


#3. voting eligibility 




name = input("enter your name :")
age = int(input("enter your age:"))

if age >= 18 :
    print("hello dear voter you are eligible to vote")
else:
    print("you are not eligible to vote")
