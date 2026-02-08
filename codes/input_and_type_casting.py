print("calculate the areaa of rectangle. Kindly enter the values:")
length=float(input("Length:"))
width=float(input("width:"))
area=length*width
print(f"The area of the rectangle is {area}")

name=input("what item would you like to buy?:")
price=float(input(f"what is the price of {name}:"))
quantity=int(input("what is the quantity:"))
total=price*quantity
print(f"your total bill for {name} is {price}*{quantity}={total}")