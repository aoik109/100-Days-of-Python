# November 4, 2023
# Learned print(), input(), len(), variables

## Purpose of this program: Username creator
print("Hi! What is your name?")
name = input()

print("Nice to meet you, " + name)
print("I will ask you questions to develop your username:")

print("What is your favorite color?")
color = input()

print("What are your favorite two numbers?")
print("First number:")
num1 = int(input())
print("Second number:")
num2 = int(input())
print("Very cool!")
num = num1 * num2

print("Lastly, what is your favorite type of animal?")
animal = input()

print("Awesome! Your username is: " + name + str(num) + animal)