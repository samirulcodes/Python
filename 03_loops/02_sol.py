# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n=int(input("Enter the number "))
sum_even=0

for i in range(1,n):
    if i%2==0:
        sum_even+=1
        
print("Sum of even number is: ",sum_even)  
 
