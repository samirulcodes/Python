''' Movie ticket pricing:
 Movie tickets are priced based on age:$12 for adults(18 and over),$8 for children,Everyone get a $2 discounton wednesday''' 
 
# This is done by Hitesh sir
age=17
day="wednesday"

price=12 if age>=18 else 8 # new syntax 

if day=="wednesday":
    price=price-2
    # price-=2
    
print("Ticket price for you on Wednesday is only $",price)

 
# This is done by me

# age=int(input("Enter you age:"))
# day=str(input("Enter day "))

# if day=="wednesday":
#     print("Everyone will get discount of $2")

# elif age>=18:
#     print("you are adult, your ticket price is $18")

# elif age<18:
#     print("your are not adult hence your ticket price is only $8")

