name = input("What is your name?\n")
birth = int(input("When were you born?\n"))
print(f"You are {2025-birth} years old, {name.title()}")
txt = 'LMaasleitbtui'
print(txt[::2])
txt = 'MsaatmiazD'
print(txt[::2])
txt = "I'am John. I am from London"
print(txt[-6:])
 
txt = "I'am John. I am from London"
print(txt[::-1])

 vowels = ["a", "i", "o", "u", "e"]
 vowels2 = "aioue"
 print(type(vowels))
 print(type(vowels2))

 text = input("Write here: ")
 count = 0
 for i in vowels:
     if i in text:
         count += text.lower().count(i)
 print(count)

numbers = input("Enter a list of numbers separated by spaces: ")
number_list = [float(num) for num in numbers.split()]
max_value = max(number_list)
print("Maximum value:", max_value)

while True:
     txt = input("so'zdi kiriting: ").strip().lower()
     if txt == txt[::-1]:
         print ("Palindrom")
     elif txt == 'stop':
         break
     else:
         print ("Not palindrom")

email = input("enter your email here")
try : 
    a = email.index("@")
    print(f"domain: {email[a+1::]}")
except:
    print ("you didn't enter an email!")  

import random
import string

letters = string.ascii_letters  # a-z + A-Z
digits = string.digits          # 0-9
special_chars = string.punctuation  # !@#$%^&*()_+...
all_chars = letters + digits + special_chars
length = int(input("Enter desired password length: "))
if length < 4:
    print("Password length should be at least 4.")
else:
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),]

    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    final_password = ''.join(password)

    print("Generated password:", final_password)
