# Input from user
num = int(input("Enter number for factorial: "))
base = int(input("Enter base for power: "))
exponent = int(input("Enter exponent: "))


# Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Recursive Power Function
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


# Calling functions
print("Factorial of", num, "=", factorial(num))
print("Power:", base, "^", exponent, "=", power(base, exponent))
