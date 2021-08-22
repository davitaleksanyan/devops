n = int(input('enter number: '))
for i in range(0, n):
    print(i ** 2)

source_list = 'Aleksanyan Davit'
new_list = ''

for a in source_list:
    if a.isupper():
        new_list += (a.lower())
    elif a.islower():
        new_list += (a.upper())
    elif a.isspace():
        new_list += a

print(source_list)
print(new_list)

a = int(input('enter first number: '))
b = int(input('enter second number: '))
print(f'The sum of two numbers: {a + b}')
print(f'The diferense of two numbers: {a - b}')
print(f'The product of two numbers: {a * b}')
