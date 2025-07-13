import json
with open('students.json', 'r') as f:
    data = json.load(f)
for student in data["Students"]:
    print("ID:", student.get("Id"))
    print("Ism:", student.get("Name"))
    print("Yosh:", student.get("Age"))
    print("Baho:", student.get("Grade"))
    print("-" * 20)


import requests
API_KEY = "API_KEY"  
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
        temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    print(f"Shahar: {city}")
    print(f"Harorat: {temperature}°C")
    print(f"Namlik: {humidity}%")
    print(f"Ob-havo: {weather}")
    print(f"Shamol tezligi: {wind_speed} m/s")
else:
    print("Xatolik yuz berdi. Status code:", response.status_code)

import json
import os

FILE_NAME = 'books.json'
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        json.dump([], f)
def load_books():
    with open(FILE_NAME, 'r') as f:
        return json.load(f)
def save_books(books):
    with open(FILE_NAME, 'w') as f:
        json.dump(books, f, indent=4)
def add_book():
    books = load_books()
    new_id = max([book["id"] for book in books], default=0) + 1
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Yil: ")

    new_book = {"id": new_id, "title": title, "author": author, "year": int(year)}
    books.append(new_book)
    save_books(books)
    print("✅ Kitob qo‘shildi!")
def update_book():
    books = load_books()
    book_id = int(input("Yangilamoqchi bo‘lgan kitob ID raqami: "))

    for book in books:
        if book["id"] == book_id:
            print(f"Hozirgi nom: {book['title']}")
            book["title"] = input("Yangi nom (qoldirish uchun Enter): ") or book["title"]
            print(f"Hozirgi muallif: {book['author']}")
            book["author"] = input("Yangi muallif (qoldirish uchun Enter): ") or book["author"]
            print(f"Hozirgi yil: {book['year']}")
            new_year = input("Yangi yil (qoldirish uchun Enter): ")
            if new_year:
                book["year"] = int(new_year)

            save_books(books)
            print("✅ Kitob yangilandi!")
            return

    print("❌ Kitob topilmadi!")

def delete_book():
    books = load_books()
    book_id = int(input("O‘chirmoqchi bo‘lgan kitob ID raqami: "))

    updated_books = [book for book in books if book["id"] != book_id]
    if len(updated_books) != len(books):
        save_books(updated_books)
        print("✅ Kitob o‘chirildi!")
    else:
        print("❌ Kitob topilmadi!")


def show_books():
    books = load_books()
    if not books:
        print("📚 Hech qanday kitob mavjud emas.")
        return

    for book in books:
        print(f"{book['id']}. {book['title']} - {book['author']} ({book['year']})")

def main():
    while True:
        print("\n📚 Kitoblar boshqaruv menyusi:")
        print("1. Kitoblar ro'yxatini ko'rish")
        print("2. Yangi kitob qo‘shish")
        print("3. Kitob ma'lumotini yangilash")
        print("4. Kitobni o‘chirish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")
if __name__ == "__main__":
    main()



import requests
import random

API_KEY = "API_KEY"  

def get_movie_by_genre(genre):
    # OMDb API qidiruv: Search orqali foydalanamiz (bu faqatgina film nomi bo‘yicha ishlaydi)
    # Buning uchun ba'zi umumiy so‘zlar bilan qidiruv qilamiz va filteringni janrga qarab qilamiz
    sample_keywords = ["love", "life", "dark", "man", "day", "night", "girl", "game"]
    random_word = random.choice(sample_keywords)

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={random_word}&type=movie"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ So‘rovda xatolik yuz berdi.")
        return

    data = response.json()

    if data.get("Response") == "False":
        print("⚠️ Hech qanday film topilmadi.")
        return

    movies = data.get("Search", [])
    matching_movies = []

    # Har bir filmni to'liq ma'lumotlari bilan olib, janrni tekshiramiz
    for movie in movies:
        movie_id = movie["imdbID"]
        detail_url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}"
        detail_response = requests.get(detail_url)
        detail_data = detail_response.json()

        if genre.lower() in detail_data.get("Genre", "").lower():
            matching_movies.append(detail_data)

    if not matching_movies:
        print(f"❌ '{genre}' janrida film topilmadi.")
        return

    selected = random.choice(matching_movies)
    print("\n🎬 Tavsiya qilingan film:")
    print(f"📌 Nomi: {selected.get('Title')}")
    print(f"📅 Yili: {selected.get('Year')}")
    print(f"🎭 Janr: {selected.get('Genre')}")
    print(f"⭐ IMDB reytingi: {selected.get('imdbRating')}")
    print(f"📝 Tavsifi: {selected.get('Plot')}")
    print(f"🔗 IMDB: https://www.imdb.com/title/{selected.get('imdbID')}/")

def main():
    genre = input("Qaysi janrdagi filmni istaysiz? (masalan: Action, Comedy, Drama): ")
    get_movie_by_genre(genre)

if __name__ == "__main__":
    main()

