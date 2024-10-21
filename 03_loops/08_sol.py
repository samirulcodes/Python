# 8. Prime Number Checker
# Problem: Check if a number is prime.

number=int(input("Enter Number: "))
is_prime=True

if number>1:
    for i in range(1,number):
        if number%i==0:
            is_prime=False
            break
print(number,"is a prime number")

