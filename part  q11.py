n = int(input("Enter the number: "))

def factorial(n):
    if n > 0:
        result = n * factorial(n - 1)
    else:
        result = 1
    return result   

print("Factorial is:", factorial(n))
