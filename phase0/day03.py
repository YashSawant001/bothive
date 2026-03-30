name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)  # Convert age to an integer
print(f"Hello, {name}! You are {age} years old.")

#simple calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if type(num1) == int and type(num2) == int:
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
    print(f"The product of {num1} and {num2} is {num1 * num2}")
    print(f"The division of {num1} and {num2} is {num1 / num2}")






