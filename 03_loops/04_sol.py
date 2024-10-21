# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str=str(input("Enter a string value: "))
rev_str=""

for char in input_str:
    rev_str=char+rev_str # swapping, actual value: rev_str=rev_str + char
    
print(rev_str)
