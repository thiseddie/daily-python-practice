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



#4. pass or fail.

nums =int(input("enter the marks you got:"))
if nums >=40 :
    print("congratulation you passed the exam enjoy")
else:
    print("better luck next time bro !!")


#5. largest of two number 

num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))

if num1>num2 :
    print("the first number is grater then the second number entered")
elif num1 == num2 :
   print("both the number entered is equal to each other")

else:
    print("the second number is grater then the first number")

