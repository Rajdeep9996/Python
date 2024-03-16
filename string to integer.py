#Write a python program to take inputs from user and perform the following operations:-
#1. Convert string to integer (in case of numbers only)
#2. Convert integer to float

user_input = input("Enter a number:" )

integer_number = int(user_input)
print("string to integer:", integer_number)

float_number = float(integer_number)
print("Integer to float:", float_number)


data_type = type[user_input, integer_number, float_number]
print(data_type)
