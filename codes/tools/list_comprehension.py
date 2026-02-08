simple_list = [1, 2, 3, 4, 5] 
squared_list = [x**2 for x in simple_list] # we are using list comprehension to create a new list with squared values of the elements in simple_list
                                            #here x holds each values of simple_list.
print(squared_list)  # Output: [1, 4, 9, 16, 25]


#supose we need to create a list of 1 to 100....now writing all of them manually is a tedious task...so we will use comprehension to create that list

one_to_hundred_list=[x for x in range(1,100,1)] # here with range we taking the range as 1 to 100...and for the last 1 we are taking the step value
print(one_to_hundred_list)  # Output: [1, 2, 3


list_with_logic= [ f'{j}{x}' for  x in range(1,11,1) for j in ('a','b','c')]
print (list_with_logic)  

battleship_board = [ f'{x}{j}' for x in ('A','B','C','D','E') for j in range(1,6,1) if f'{x}{j}'!='C3']
print(battleship_board)  # simulating a hit on E4

 # I need to learn more about the comprehension