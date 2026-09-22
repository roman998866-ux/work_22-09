# Импортируем tkinter для окна, кнопок и подписей
from tkinter import *
# Импортируем ttk для полей ввода
from tkinter import ttk
# Импортируем psycopg для PostgreSQL
import psycopg


# Это функция. Запустится по нажатию кнопки
def save_book():
    # Это берёт текст из поля Название
    nazvanie = entry_name.get()
    # Это берёт текст из поля Автор
    avtor = entry_author.get()
    # Это берёт год и делает число
    god = int(entry_year.get())
    # Это берёт минуты и делает число
    stranic = int(entry_pages.get())

    conn = psycopg.connect(
        host="localhost",
        dbname="books_lab",
        user="postgres",
        password="Admin"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (Название, Автор, Год, Страниц) VALUES (%s, %s, %s, %s);",
        (nazvanie, avtor, god, stranic)
    )
    conn.commit()
    cur.close()
    conn.close()
    # Это пишет результат в подпись внизу окна
    label["text"] = "Добавлено: " + nazvanie


# Это создаёт окно
root = Tk()
root.title("Добавить книгу")
root.geometry("280x280")

ttk.Label(root, text="Название").pack(anchor=NW, padx=6, pady=2)
entry_name = ttk.Entry()
entry_name.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Автор").pack(anchor=NW, padx=6, pady=2)
entry_author = ttk.Entry()
entry_author.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Год").pack(anchor=NW, padx=6, pady=2)
entry_year = ttk.Entry()
entry_year.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Страниц").pack(anchor=NW, padx=6, pady=2)
entry_pages = ttk.Entry()
entry_pages.pack(anchor=NW, padx=6, pady=2)

# command=save_book — по клику вызвать функцию
btn = ttk.Button(text="Добавить", command=save_book)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

# Это держит окно открытым
root.mainloop()