# Transportation mode selection
# dist<3: go by walk , dist:<20 , go by bike and if dist greater than 20 the go by car, write a python prog.

# Done by me
distance=int(input("Enter distance: "))

if distance<3:
    print("By walk")
    
elif distance<=20:
    print("By Bike")
    
else:
    print("By Car")
    
    
# done by hitesh sir

# distance = 5

# if distance < 3:
#     transport = "Walk"
# elif distance <= 15:
#     transport = "Bike"
# else:
#     transport = "Car"

# print("AI recommends you the transport of: ", transport)
