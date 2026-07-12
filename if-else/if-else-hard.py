#1. login system.


username = input("enter the username :")
password = input("enter the password :")


if username == "admin" and password == "python123" :
    print("login successful")
elif username == "admin" and password ! == "pyhon123" :
  print("passowrd is incorrect")
elif username ! == "admin" and password == "pyhton123" :
    print("username is incorrect")


#2. electricity bill calculator


unit = int(input("enter the unit consumed :"))

if unit <=100 :
    print("thr bill amount is 0") 
elif unit > 101 and unit <= 200 :
    bill = (unit - 100)*5
    print ("the bill amount is :",bill)
    elif unit > 201 and unit <=300 :
    bill = (unit - 200)*7
    print("the bill amount is :",bill)
else:
    bill = (unit - 300)*10
    print("the bill amount is :",bill)



#3. atm withdrawal system 



balance = int(input("enter the account balance :"))
amount = int(input("enter the amount you want to withdraw :"))
 if balance <= amount :
     print("insufficient balance")
 elif balance % 100 != 0 :
print("you have entered the wrong amount please enter the amount in mutiple of 100")
else :
  balance -= amount
print("please collect your cash")
print("your remaining balance is :", balance)



#4. BMI calculator.


height = float(input("enter your height in meter :"))
weight = float(input("enter your weight in kg :"))

bmi = wight / (height*height)
print("your bmi is :",bmi)

if bmi < 18.5 :
    print("you are underweight")
elif bmi >= 18.5 and bmi <25 :
    print("you are normal")
elif bmi >=25 and bmi <= 30 :
    print("you are overweight")
else :
    print("obese")




#5. number guessing hint
