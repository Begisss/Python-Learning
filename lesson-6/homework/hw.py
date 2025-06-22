def insert_underscores(txt):
    result = ''
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in 'aeiouAEIOU_' or (i + 1 < len(txt) and txt[i + 1] in 'aeiouAEIOU_'):
                if i + 1 < len(txt):
                    i += 1
                    result += txt[i]
                if i + 1 < len(txt):
                    result += '_'
                count = 0
            else:
                result += '_'
                count = 0
        i += 1
    return result
print(insert_underscores("hello"))      
print(insert_underscores("keyboard"))  

n = int(input())
for i in range(n):
    print(i ** 2)

i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

num = int(input("Enter number: "))
i = 1
total = 0
while i <= num:
    total += i
    i += 1
print("Sum is:", total)

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i += 1

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 70 < num <= 150:
        print(num)

num = 75869
count = 0
while num != 0:
    num //= 10 
    count += 1
print("Total digits:", count)

for i in range(5, 0, -1):      
    for j in range(i, 0, -1): 
        print(j, end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

for i in range(-10, 0):
    print(i)

for i in range(1, 6):
    print(i)
else:
    print("Done")

for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

n_terms = 10
a, b = 0, 1
for _ in range(n_terms):
    print(a)
    a, b = b, a + b

num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = list((c1 - c2).elements()) + list((c2 - c1).elements())
    return result
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))


