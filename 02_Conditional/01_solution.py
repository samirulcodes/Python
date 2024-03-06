# 1. Age Group Categorization

age=int(input("Enter your age: "))

if age<13:
    print("Child")
elif age>=13 and age<=20:
    print("Teenager")

elif age>=21 and age<=50:
    print("Young")

else:
    print("Senior Citizen")