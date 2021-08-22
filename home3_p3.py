import textwrap as tw

source_lst = input('Enter some string: ')
target_lst = input('Enter string for search: ')
sl = len(source_lst)
tl = len(target_lst)
count = 0
for i in range(sl - tl + 1):
    j = 0
    while j < tl:
        if source_lst[i + j] != target_lst[j]:
            break
        j += 1
    if j == tl:
        count += 1
        j = 0
print(count)

testString1 = "Hello World!"
res = tw.wrap(testString1, 4)
for i in res:
    print(i)

year = int(input("Enter year: "))
if year % 4 == 0 and year % 400 == 0:
    print(f'{year} is leap')
else:
    print(f'{year} is not a leap')
