try:
    a = 10
    b = 0
    c = a / b
    print("Natija:", c)
except ZeroDivisionError:
    print("Xatolik: Nolga bo'lish mumkin emas.")

try:
    user_input = input("Butun son kiriting: ")
    number = int(user_input)
    print(f"Siz kiritgan son: {number}")
except ValueError:
    print("Xatolik: Bu to‘g‘ri butun son emas!")

try:
    filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

try:
    x = input("Birinchi sonni kiriting: ")
    y = input("Ikkinchi sonni kiriting: ")
    if not (x.replace('.', '', 1).isdigit() and y.replace('.', '', 1).isdigit()):
        raise TypeError("Faqat son kiritish kerak!")
    x = float(x)
    y = float(y)
    print(f"Kiritilgan sonlar: {x} va {y}")
    print(f"Ularning yig'indisi: {x + y}")
except TypeError as te:
    print(f"Xatolik: {te}")

try:
    filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except PermissionError:
    print("Xatolik: Faylga kirishga ruxsat yo‘q.")

try:
    my_list = [10, 20, 30]
    index = int(input("Index kiriting (0-2): "))
    print("Qiymat:", my_list[index])
except IndexError:
    print("Xatolik: Ro‘yxatda bunday index yo‘q.")


try:
    number = int(input("Iltimos, son kiriting: "))
    print("Siz kiritgan son:", number)
except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi (Ctrl + C bosildi).")


try:
    a = 10
    b = 0
    result = a / b
    print("Natija:", result)
except ArithmeticError:
    print("Xatolik: Arifmetik xato yuz berdi (ehtimol nolga bo‘linmoqda).")

try:
    filename = input("Fayl nomini kiriting: ")
    with open(filename, 'r', encoding='ascii') as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)
except UnicodeDecodeError:
    print("Xatolik: Fayl kodlashida muammo bor (UnicodeDecodeError).")

try:
    my_list = [1, 2, 3]
    my_list.upper()  # noto‘g‘ri: `list`da `.upper()` yo‘q
except AttributeError:
    print("Xatolik: Bu ob'ekt bunday metodga ega emas (AttributeError).")

# 1. Read entire text file
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 2. Read first n lines of a file
n = 3
with open("example.txt", "r", encoding="utf-8") as file:
    for i in range(n):
        print(file.readline(), end="")

# 3. Append text to a file and display
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\nQo‘shilgan yangi satr.")
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 4. Read last n lines of a file
n = 3
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")

# 5. Read file line by line and store into a list
with open("example.txt", "r", encoding="utf-8") as file:
    lines_list = file.readlines()
    print(lines_list)

# 6. Read file line by line and store into a variable
with open("example.txt", "r", encoding="utf-8") as file:
    all_text = "".join(file.readlines())
    print(all_text)

# 7. Read file line by line and store into an array (same as list)
with open("example.txt", "r", encoding="utf-8") as file:
    array = file.readlines()
    print(array)

# 8. Find the longest words
with open("example.txt", "r", encoding="utf-8") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Eng uzun so‘z:", longest)

# 9. Count number of lines
with open("example.txt", "r", encoding="utf-8") as file:
    line_count = sum(1 for _ in file)
    print("Satrlar soni:", line_count)

# 10. Count frequency of words
from collections import Counter
with open("example.txt", "r", encoding="utf-8") as file:
    words = file.read().replace(",", " ").split()
    word_freq = Counter(words)
    print(word_freq)

# 11. Get file size
import os
print("Fayl o‘lchami (bayt):", os.path.getsize("example.txt"))

# 12. Write a list to a file
lines = ["Salom\n", "Yaxshimisiz\n", "Python yaxshi dasturlash tili.\n"]
with open("newfile.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

# 13. Copy contents of one file to another
with open("example.txt", "r", encoding="utf-8") as src, open("copy.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())

# 14. Combine lines from two files
with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "r", encoding="utf-8") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15. Read a random line
import random
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Tasodifiy satr:", random.choice(lines).strip())

# 16. Assess if a file is closed
f = open("example.txt", "r", encoding="utf-8")
print("Fayl yopilganmi:", f.closed)
f.close()
print("Fayl yopilganmi:", f.closed)

# 17. Remove newline characters
with open("example.txt", "r", encoding="utf-8") as file:
    clean_lines = [line.strip() for line in file]
    print(clean_lines)

# 18. Count words in a file
with open("example.txt", "r", encoding="utf-8") as file:
    text = file.read().replace(",", " ")
    word_count = len(text.split())
    print("So‘zlar soni:", word_count)

# 19. Extract characters from multiple files into a list
import glob
chars = []
for filename in glob.glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        chars.extend(list(file.read()))
print(chars)

# 20. Generate 26 text files A.txt to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")

# 21. Create file with alphabet, n letters per line
n = 5
with open("alphabet.txt", "w") as file:
    alphabet = string.ascii_uppercase
    for i in range(0, len(alphabet), n):
        file.write(alphabet[i:i+n] + "\n")

