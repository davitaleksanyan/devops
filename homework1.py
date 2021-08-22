'''
#1  Create a program that takes two numbers as input and print their sum.
# print(int(input('Enter first number: ')) + int(input('Enter second number: ')))
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f'The sum of two numbers is: {a + b}')
#2 2.  Write a program that takes an integer minutes as input and converts it to seconds and print result.

minutes = int(input('Enter minutes: '))
print(f'The {minutes} minute\'s equal to {minutes*60} seconds')

#3.  Create a program that prints True when num1 is equal to num2; otherwise print False. num1 and num2 get from user input
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(a == b)

# 4.  Get input from user, print is input odd or even
a = int(input('Enter number: '))
if a / 2 == 0:
    print(f'The input number {a} is even')
else:
    print(f'The input number {a} is odd')

#5. Create a program that takes a number as input and print negative of that number.
#    Return negative numbers without any change.
a = int(input('Enter number: '))
a = -a
print(f'the negativ is: {a}')
# 6. Create a program that takes a number as an input, increments the number by +1 and pints the result.
a = int(input('Enter  number: '))
a += 1
print(f'the new a is: {a}')

#7 Create a program that takes an integer and prints True if it's divisible by 100, otherwise print False.
a = int(input('Enter number: '))
if a % 100 == 0:
    print(True)
else:
    print(False)
'''
# 8. Create a program that takes the number of wins,
# draws and losses and calculates the number of points a football team has obtained so far.
wins = int(input('Enter wins: '))
draws = int(input('Enter draws: '))
loses = int(input('Enter loses: '))
points = wins*3 + draws + loses
print(f'Points is: {points}')
# 9. Create a program that calculates the area of a rectangle. If the inputs are invalid, your program must print -1.
