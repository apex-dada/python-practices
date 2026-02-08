#while loop == execute some code while some condition remains true
#while loop creates a infinite loop if we dont create a escape. its the individual characteristic of while loop. which makes it different than if else loop.
# name=input("enter your name:")
# while name =="":
#     print("you did not entered your name")
#     name=input("enter your name:")
#
# print(f"hello {name}")

#---------------------------------------------

# age=int(input("enter your age:"))
#
# while age>100 or age<0:
#     print("age must be between 1 to 99")
#     age=int(input("kindly submit your age correctly :"))
# print(f"your age is {age}")

# food=input("enter your desired food :")
#
# while not food=="q":
#     print(f"your desired food is {food}")
#     food=input("enter your another desired food(enter q to close) :")
# print("thank YOU!")

#>>>>>>>>>>>>>>>EXERCISE<<<<<<<<<<<<<<<<<<<
#Compound interest calculator

principleBalance=0
interestRate=0
time=0

while principleBalance<=0:
    principleBalance=float(input("Enter your initial or principle balance:"))
    if principleBalance <=0 :
        print("Principle balance can not be zero or negative.")

while interestRate<=0 or interestRate>=50:
    interestRate=float(input("enter your interest rate:"))
    if interestRate<=0 or interestRate>=50:
        print("interest rate can not be zero or negative and more than 50%")

while time<=0:
    time=int(input("enter time:"))
    if time<=0:
        print("time can not be zero or negative.")

print(f"you principle balance is {principleBalance}")
print(f"you interest rate is {interestRate}%")
print(f"your period of saving is {time}")

finalAmmount=principleBalance*pow((1+interestRate/100),time)

genaratedInterest=finalAmmount-principleBalance
print(f"\n The final amount for your balance is: {finalAmmount}")
print(f"You generated {genaratedInterest} in {time} years")

#the problem with this code is user cannot add zero cause we initialized our values by zero...when we give condition while>0 we do not enter the loop...we skip the loop to the answer .so  if we want our user to enter zero than we can write it like this:
#note: we are giving True condition in the while loop. it means the while loop run for infinite until we break it. 

principleBalance=0
interestRate=0
time=0

while True:
    principleBalance=float(input("Enter your initial or principle balance:"))
    if principleBalance <0 :
        print("Principle balance can not be negative.")
    else:
        break

while True:
    interestRate=float(input("enter your interest rate:"))
    if interestRate<0 or interestRate>=50:
        print("interest rate can not be negative and more than 50%")
    else:
        break

while True:
    time=int(input("enter time:"))
    if time<0:
        print("time can not be negative.")
    else:
        break

print(f"you principle balance is {principleBalance}")
print(f"you interest rate is {interestRate}%")
print(f"your period of saving is {time}")

finalAmmount=principleBalance*pow((1+interestRate/100),time)

genaratedInterest=finalAmmount-principleBalance
print(f"\n The final amount for your balance is: {finalAmmount}")
print(f"You generated {genaratedInterest} in {time} years")