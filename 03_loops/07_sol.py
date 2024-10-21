# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10

while True:
    num=int(input("Enter number b/w 1 and 10: "))
    #  if num>=1 and num<=10:    # line 6 and 7 both are same
    if 1<= num <=10:
   
        print("done successfully")
    
    else:
        print("Invalid Number, try again")

