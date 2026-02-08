#in the conventional way :

user_age=11

if user_age>=18:
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")
    
# using single line if statements

user_status="eligible for vote" if user_age>=18 else "not eligible for vote"

print(user_status)