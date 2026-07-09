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

    
