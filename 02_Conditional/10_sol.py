# recommend a type of pet food based on the pet specie's and age(eg: Dog<2 yrs- puppy food, Cat>5 yrs- senior cat food)

pet_age=int(input("Enter pet age: "))

if pet_age<2:
    print("Dog age is",pet_age,"so provide PUPPY FOOD")
    
elif pet_age<=5:
     print("Cat age is",pet_age,"so provide senior CAT FOOD")
     
else:
    print("Now the pet age is",pet_age,"so you can give meat also")