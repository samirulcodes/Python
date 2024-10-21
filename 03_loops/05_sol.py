# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

inp_str=str(input("Enetr a String value: "))

for char in inp_str:

    if inp_str.count(char)==1:
        print("Char is: ",char)
        
