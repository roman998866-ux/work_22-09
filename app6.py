import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="books_lab",
    user="postgres",
    password="Admin"
)
cur = conn.cursor()

# Это спрашивает текст у пользователя в консоли
nazvanie = input("Название: ")
avtor = input("Автор: ")
# int — перевод в число, потому что в таблице тип INT
god = int(input("Год: "))
stranic = int(input("Страниц: "))

# Это добавляет строку. %s — места под значения
cur.execute(
    "INSERT INTO books (Название, Автор, Год, Страниц) VALUES (%s, %s, %s, %s);",
    (nazvanie, avtor, god, stranic)
)

# Это сохраняет запись. Без commit строка пропадёт
conn.commit()

print("Строка добавлена.")

cur.execute("SELECT * FROM books;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()