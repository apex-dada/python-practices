#f Strings
user_name="woaej"
user_age=22
user_city="dhaka"
user_information=' woaej is 22 years old and lives in dhaka'

bad_approch=user_name +" is "+str(user_age)+" years old and lives in "+user_city
print(bad_approch)

#good approch : f strings
user_information_f=f"{user_name} is {user_age} years old and lives in {user_city}"
print(user_information_f)