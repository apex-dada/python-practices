#without using lambda functions
def double(x):
    return x * 2
print(double(5))  

#with lambda functions

double_value = lambda num : num * 2
print(double_value(20))

#where we use the lamda functions the most?? suppose we have a list of tuples with name and age . and now we want to sort the list based on the age
# if we simply use sort function then it will take the first element of the tuple as a key and just sort it...suppose we dont have age in the first element...then 
#how we will sort it based on age? here comes the use of lambda function.
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people_without_lambda= sorted(people)

#without lambda function
print(sorted_people_without_lambda)  #here it will sort based on the first element of the tuple which is name....which we dont want

#again with lambda function
sorted_people_with_lambda_function= sorted(people , key = lambda person: person[1]) # here we are using lambda function to extract the age from each tuple and use it as the key for sorting
print(sorted_people_with_lambda_function)  # now it will sort based on the age which is the second element of the tuple

