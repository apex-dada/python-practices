x=3.1416
y=-4
z=5
result= round(x) #rounds the given value
result2=abs(y) #abs(value) gives the absolute value. means it will give the value needed to go zero
result3=pow(4,3) #pow() is used for answer the of to the power of a value.4^3 in this case
result4=max(3,6,9) #max() shows the maximum value between various values.
result5=min(3,6,9) #min() shows  the minimum value between various values

print(result)
print(result2)
print(result3)
print(result4)
print(result5)


import math
x=9
print(math.pi) #math.pi gives the value of pi
print(math.e) #math.e gives the value of exponential
result=math.sqrt(x) # math.sqrt(value) gives the square root value of given value
print (result)
result=math.ceil(x) #math.ceil gives the ceiling value. ex: 3.12 will be 4
result=math.floor(x) #math.floor gives the flooring value. ex: 3.12 will be 3



# practice 1
# calculate the value of circumference
import math
radius=float(input("enter the value of radius:"))
c=2*math.pi*radius
print(f"the value of the circumference is {round(c , 2)}")



# practice 2
# calculate the value of area of a circle
import math
radius=float(input("enter the value of radius:"))
area=math.pi*pow(radius,2)
print(f"the value of the area is {round(area , 2)}")


# practice 3
# calculate the hypotenuse of a triangle
import math
a=float(input("enter the value of one side of triangle:") )
b=float(input("enter the value of another side of triangle:"))
hypotenuse=math.sqrt((pow(a,2)+pow(b,2)))
print(f"the value of the hypotenuse is {round(hypotenuse,3)}")

