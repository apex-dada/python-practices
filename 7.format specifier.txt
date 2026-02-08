#format specifiers== {value:flags} format a value based on what flag are inserted

price1=3.14169
price2=-987.65
price3=12.34
price4=99999999
print(f"price 1 is {price1:.2f}") # {value:f} will create decimal value....if we want three or four decimal places to print we can write 3f/4f
print(f"price 2 is {price2:10}") # {value: number} will allocate space for the value as given number. it will include the given value as a allocated space when allocating
print(f"price 2 is {price2:010}") #adding a zero behind the value of flag will add zero padding
print(f"price 3 is {price3:<10}") # < behind the flag will justify/align the value to left
print(f"price 3 is {price3:>10}") # > behind the flag will justify/align the value to Right
print(f"price 3 is {price3:^10}") # ^ behind the flag will justify/align the value to Right

print(f"price 1 is {price1:+}") # {value:+} will print + sign with the positive values and - with negetive
print(f"price 2 is {price2:+}") # {value:+} will print + sign with the positive values and - with negetive
print(f"price 3 is {price3:+}") # {value:+} will print + sign with the positive values and - with negetive
print(f"price 4 is {price4:,}") # {value:,} will add commas behind the thousand  numbers

print(f"price 4 is {price4:+,.2f}") #combaining 3 flags. *****important*****
# correct order to use formal specifiers {value:[fill][align][sign][#][0][width][,][.precision][type]}

print(f"price 1 is {price1:0>+10,.2f}")


