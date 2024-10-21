# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# counting total +ve num
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count=0

for num in numbers:
    if num>0:
        positive_num_count+=1

print("finally count of positive number is: ",positive_num_count)


# counting total -ve num
negative_num_count=0
for num in numbers:
    if num<0:
        negative_num_count+=1

print("finally count of negative number is: ",negative_num_count)