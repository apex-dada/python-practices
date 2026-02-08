#dictionary = collection of {key:value} pairs.
#              ordered and changeable. no duplicates

captital={"usa": "washington",
          "Bangladesh":"dhaka",
          "China":"beijing",
          "Russia":"moscow"}
print(captital.get("Bangladesh"))
print(captital.get("usa"))
print(captital.get("japan"))

#__________Check Wether the key is available in dictionary_____________

if captital.get("Bangladesh"):
    print(f"available. the capital is: {captital.get("Bangladesh")}")
else:
    print("not available")

if captital.get("Japan"):
    print(f"available. the capital is: {captital.get("Bangladesh")}")
else:
    print("not available")

#________Add keys to dictionary_____________
captital.update({"germany":"berlin"})
print(captital.get("germany"))

#________Delete keys from dictionary_____________
captital.pop("China") #to delete a specific item
captital.popitem() #to delete latest added item... lifo (last in first out)

#--------------TO print all the keys available-----------------
key=captital.keys()
print(key)

#or we can write it in better way without the bracket and colons

for allKey in captital.keys():
    print(allKey, end=" ")

#---------print all the values from dictionary--------------
value=captital.values()
print(value)
#or we can write it in better way without the bracket and colons
for allValues in captital.values():
    print(allValues , end=" ")

#________printing all the items from dictionary___________
item=captital.items()
print(item)
#or we can write it in better way without the bracket and colons
for keys,values in captital.items():
    print(f"{keys}:{values}")
#______________________exercise_________________________


#food menu program with dictionary
menu = {
    "burger": 5.99,
    "pizza": 3.99,
    "pasta": 7.25,
    "sushi": 12.99,
    "salad": 4.50,
    "taco": 3.75,
    "fried chicken": 6.80,
    "ice cream": 2.99,
    "steak": 14.99,
    "ramen": 9.10}
cart=[]
total=0
print("-------------menu-------------")
for keys,vlaues in menu.items():
    print(f"{keys:15}: {vlaues:.2f}")
print("------------------------------")
while True:
    food=input("select an item(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------------CART-------------")
for foods in cart:
    total += menu.get(foods)
    print(foods,end=" ")
print(f"\nthe total is: {total:.2f} ")
print("------------------------------")