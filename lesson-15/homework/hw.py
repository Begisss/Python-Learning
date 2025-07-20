import sqlite3

connection = sqlite3.connect("animals.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER)
""")

connection.commit()
connection.close()

print("Database and Roster table created successfully.")

import sqlite3

connection = sqlite3.connect("animals.db")
cursor = connection.cursor()

data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

connection.commit()
connection.close()

print("Data inserted successfully into Roster table.")
data

import sqlite3

connection = sqlite3.connect("animals.db")
cursor = connection.cursor()

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

connection.commit()
connection.close()

print("Name updated successfully.")
data

import sqlite3

connection = sqlite3.connect("animals.db")
cursor = connection.cursor()

cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()
for row in results:
    print("Name:", row[0], "| Age:", row[1])

connection.close()
data
