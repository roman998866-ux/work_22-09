from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psycopg

PG_PASSWORD = "Admin"


# Это подключение к базе пользователей
def connect_users():
    return psycopg.connect(
        host="localhost",
        dbname="user_ui_db",
        user="postgres",
        password=PG_PASSWORD
    )


# Это подключение к базе книг
def connect_books():
    return psycopg.connect(
        host="localhost",
        dbname="books_lab",
        user="postgres",
        password=PG_PASSWORD
    )


# Это создаёт таблицу users, если её нет
def create_users_table():
    conn = connect_users()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (Логин TEXT, Пароль TEXT);")
    conn.commit()
    cur.close()
    conn.close()


# Это регистрация: INSERT логина и пароля
def register():
    login = entry_login.get()
    password = entry_password.get()
    if login == "" or password == "":
        messagebox.showerror("Ошибка", "Введите логин и пароль")
        return
    conn = connect_users()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE Логин = %s;", (login,))
    if cur.fetchone() is not None:
        messagebox.showerror("Ошибка", "Такой логин уже есть")
        cur.close()
        conn.close()
        return
    cur.execute(
        "INSERT INTO users (Логин, Пароль) VALUES (%s, %s);",
        (login, password)
    )
    conn.commit()
    cur.close()
    conn.close()
    messagebox.showinfo("Готово", "Регистрация прошла. Нажмите Войти.")


# Это вход: ищем пару логин+пароль
def login():
    login_value = entry_login.get()
    password_value = entry_password.get()
    conn = connect_users()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE Логин = %s AND Пароль = %s;",
        (login_value, password_value)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")
        return
    # Это закрывает окно входа
    auth_window.destroy()
    # Это открывает форму книг
    open_books_window()


def open_books_window():
    win = Tk()
    win.title("Добавить книгу")
    win.geometry("280x280")

    def save_book():
        nazvanie = entry_name.get()
        avtor = entry_author.get()
        god = int(entry_year.get())
        stranic = int(entry_pages.get())
        conn = connect_books()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (Название, Автор, Год, Страниц) VALUES (%s, %s, %s, %s);",
            (nazvanie, avtor, god, stranic)
        )
        conn.commit()
        cur.close()
        conn.close()
        label["text"] = "Добавлено: " + nazvanie

    ttk.Label(win, text="Название").pack(anchor=NW, padx=6, pady=2)
    entry_name = ttk.Entry(win)
    entry_name.pack(anchor=NW, padx=6, pady=2)
    ttk.Label(win, text="Автор").pack(anchor=NW, padx=6, pady=2)
    entry_author = ttk.Entry(win)
    entry_author.pack(anchor=NW, padx=6, pady=2)
    ttk.Label(win, text="Год").pack(anchor=NW, padx=6, pady=2)
    entry_year = ttk.Entry(win)
    entry_year.pack(anchor=NW, padx=6, pady=2)
    ttk.Label(win, text="Страниц").pack(anchor=NW, padx=6, pady=2)
    entry_pages = ttk.Entry(win)
    entry_pages.pack(anchor=NW, padx=6, pady=2)
    ttk.Button(win, text="Добавить", command=save_book).pack(anchor=NW, padx=6, pady=6)
    label = ttk.Label(win)
    label.pack(anchor=NW, padx=6, pady=6)
    win.mainloop()


create_users_table()

auth_window = Tk()
auth_window.title("Вход")
auth_window.geometry("280x200")

ttk.Label(auth_window, text="Логин").pack(anchor=NW, padx=6, pady=2)
entry_login = ttk.Entry(auth_window)
entry_login.pack(anchor=NW, padx=6, pady=2)
ttk.Label(auth_window, text="Пароль").pack(anchor=NW, padx=6, pady=2)
entry_password = ttk.Entry(auth_window, show="*")
entry_password.pack(anchor=NW, padx=6, pady=2)

ttk.Button(auth_window, text="Войти", command=login).pack(anchor=NW, padx=6, pady=6)
ttk.Button(auth_window, text="Регистрация", command=register).pack(anchor=NW, padx=6, pady=2)

auth_window.mainloop()