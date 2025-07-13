from datetime import datetime, date
from dateutil.relativedelta import relativedelta
birth_input = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD formatda): ")
try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = date.today()
    age = relativedelta(today, birth_date)
    print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

from datetime import datetime, date
birth_input = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD formatda): ")
ry:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = date.today()
    this_year_birthday = date(today.year, birth_date.month, birth_date.day)
    if this_year_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    else:
        next_birthday = this_year_birthday
    days_left = (next_birthday - today).days
    print(f"Sizning navbatdagi tug‘ilgan kuningizgacha {days_left} kun qoldi.")
except ValueError:
    print("Noto‘g‘ri format! Sanani YYYY-MM-DD shaklida kiriting.")

from datetime import datetime, timedelta
current = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))
try:
    start_time = datetime.strptime(current, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(hours=hours, minutes=minutes)
    print("Uchrashuv tugash vaqti:", end_time.strftime("%Y-%m-%d %H:%M"))
except ValueError:
    print("Format noto‘g‘ri!")

from datetime import datetime
import pytz
current_time = input("Vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_zone = input("Hozirgi vaqt zonasi (masalan, Asia/Tashkent): ")
to_zone = input("Qaysi vaqt zonasiga o‘tkazmoqchisiz (masalan, US/Eastern): ")
try:
    tz_from = pytz.timezone(from_zone)
    tz_to = pytz.timezone(to_zone)
    dt_naive = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    dt_local = tz_from.localize(dt_naive)
    dt_converted = dt_local.astimezone(tz_to)
    print("Yangi vaqt:", dt_converted.strftime("%Y-%m-%d %H:%M"))
except Exception as e:
    print("Xatolik:", e)

import time
from datetime import datetime
future = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future, "%Y-%m-%d %H:%M:%S")
while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Vaqt tugadi!")
        break
    print("Qolgan vaqt:", remaining)
    time.sleep(1)

import re
email = input("Email manzilini kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Email manzili to‘g‘ri!")
else:
    print("Email noto‘g‘ri formatda.")

number = input("Telefon raqamini kiriting (faqat raqamlar): ")
if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatlangan:", formatted)
else:
    print("Raqam noto‘g‘ri!")

import re
password = input("Parolni kiriting: ")
if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'[0-9]', password)):
    print("Parol kuchli!")
else:
    print("Parol zaif: kamida 8 ta belgi, katta harf, kichik harf va raqam bo‘lishi kerak.")

text = "Bu oddiy matn namunasi. Matnda so'zlarni izlash mumkin."
word = input("Qaysi so‘zni qidiramiz? ").lower()
matches = [w for w in text.lower().split() if word in w]
print(f"Topilgan so‘zlar: {matches}")

import re
text = input("Matnni kiriting: ")
# Formatlar: 2025-07-13, 13/07/2025, 13-07-2025
pattern = r'\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b'
dates = re.findall(pattern, text)
print("Topilgan sanalar:", dates)

