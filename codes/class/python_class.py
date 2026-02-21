# a basic class in python
class BasicClass:
    test_var = "hello world" 
    another_var = 'some value'
    def test_function(self) :
        print("test function called")
    
# create an instance of the class
test = BasicClass()
print(test.test_var)  # Output: hello world
test.another_var="modified Value"
print(test.another_var)  # Output: some value

test2= BasicClass()
print(test2.another_var)

test2.test_function()
#we have modified the value of another_var for the test instance only...the class variable remains unchanged for other instances
