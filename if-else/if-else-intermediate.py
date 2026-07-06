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


#2. find the year is wether a leap year or not.


year = int(input("enter the year :"))

if year % 400 ==0 :
    print("the year entered is a leap year")
elif year % 100 ==0 :
    print("the year entered is not a leap year")
elif year % 4 ==0 :
    print("the year entered is a leap year")
else:
    print("the year is not leap year")



#3. grade calculator. 

marks = int(input("enter the marks you got :"))

if marks >= 90 and marks <= 100 :
    print("congo... you got 'A' grade ")
elif marks >=80 and marks <=89 :
    print("congo.... you got 'B' grade")
elif marks >=70 and marks <=79 :
    print("congoo...you got 'C' grade . do better")
elif marks >=60 and marks <=69 :
    print("congo.... you got 'C' grade")
else:
    print("better luck next time")




#4.age category


age = int(input("enter the age :"))

if age >=0 and age <=12 :
    print("As you entered the age you comes in a child category")
elif age >=13 and age <=19 :
    print("As you entered the age you comes in a teenager category")
elif age >=20 and age <=59 :
    print("The age you entered. you comes in adult category")
else :
     print("As you entered the you comes in senior citien category")




#5. divisibility check.

num = int(input("enter the number you want to check :))

  if num % 5 == 0 and num % 3 == 0:
                print("the number you entered is divisible by both")
                elif num % 5 ==0 :
                print("the number you entered is divisible by 5")
                elif num % 3 == 0 :
                print("the number you entered is divisible by 3")
                else :
                print("not divisible by either")
