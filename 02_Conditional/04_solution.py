'''
Fruits ripeness checker:
determine if a fruit is ripe,overripe,or unripe based on its color.(eg: Banana:Green-Unripe,Yellow-Ripe,Brown-Overripe)
'''
# Done by me
color=str(input("Enter the color for checking fruits condition: "))
fruit=str(input("Enter fruits name: "))

if color=="green":
    if fruit=="banana":
     print("Unripe")

elif color=="yellow":
    print("Fruits is Ripe")

elif color=="brown":
    print("Fruits is Overripe")
else:
    print("enter the fruits name carefully")
    
    
# checking condition for another fruit

# if color=="green":
#     if fruit=="mango":
#      print("sour")

# elif color=="yellow":
#     print("sweet")

# elif color=="darkGreen":
#     print("Malda Mango")

# else:
#     print("enter the fruits name carefully")


# Done by hitesh sir

# fruit="Banana"
# color="Green"

# if fruit=="Banana":
#     if color=="Green":
#         print("Unripe")
#     elif color=="Yellow":
#         print("Ripe")
#     elif color=="Brown":
#         print("OverRipe")
    