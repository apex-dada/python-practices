#function is defined with def keyword . fucntion can return a value or just perform a task

def my_first_fuction():
    print("this is my first function")

my_first_fuction()  #function call

#why we use functions? supoose you want to calculate the area of rectangles .... 
# will you write the same formula / code again and again?
#here comes the function... we can define the code once and call it whenever we want..

def area_of_rectangle(length,width):
    area=length*width
    print(f"the area of rectangle is {area}")
    
area_of_rectangle(5,10)  #function call with arguments
area_of_rectangle(7,3)   #function call with different arguments

#returning a value

def lets_return_value():
    return "here is the returned value" 

message=lets_return_value()  #storing the returned value in a variable
print(message)

#we can use parameter and return value together
#suppose we want to take input mail accounts...now we made a fuction for that.
#but every time we need the write gmail.com manually....but we dont need to do that if add the gmail.com the the returned value

def enter_your_mail(username):  #username is out parameter here
    print(username +"@gmail.com")

enter_your_mail("kaziwoaej")  #kaziwoaej is out argument here
enter_your_mail("exampleuser")  #exampleuser is our argument here


#*************** we can add any number of parameters in a function using * sign  ****************

#supose we want to create a fuction which will store your siblings name. but  we dont know how many siblings you have.so we can use * sign to add any number of parameters

def store_siblings(*siblings):  #*siblings means we can add any number of parameters
    print("your siblings are:")
    for sib in siblings:
        print(sib)
store_siblings("woaej","wasif","jaima")
      
#but now we want to add texts before each sibling name like brother: woaej , sister: jaima etc

def store_siblings_with_relation(*siblings):  #**siblings means we can add any number of key value pair parameters
    print(" brother : " , siblings[0])
    print(" sister : " , siblings[1])
store_siblings_with_relation("wasif","jaima")

#the same thing we can apply in the calculator function

def calculator(*numbers):
    total=0
    for num in numbers:
        total+=num
    print(f"the total sum is {total}")
calculator(10,20,30,40,50)