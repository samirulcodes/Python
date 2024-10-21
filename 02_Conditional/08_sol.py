# check if a password is weak, medium or stronger.Criteria <6 char(weak),6-10 char(medium) ,>10 char(strong)

# done by me

password=str(input("Enter password "))

if len(password)<6:
    print("password is weak")
    
elif len(password)>=6 and len(password)<=10:
    print("password is medium")
    
else:
    print("password is strong")




# done by hitesh sir

# password = "Secure3P@ss"
# password_length = len(password)   #optional line

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is: ", strength)
