try:
    year_input = int(input("Yilni kiriting: "))
    if is_leap(year_input):
        print(f"{year_input} kabisa (kabisa) yili.")
    else:
        print(f"{year_input} oddiy yil.")
except ValueError:
    print("Iltimos, butun son kiriting.")

n = int(input("Enter a number: "))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
if a > b:
    start = b
    end = a
else:
    start = a
    end = b
if start % 2 != 0:
    start += 1
even_numbers = list(range(start, end + 1, 2))
print(even_numbers)
