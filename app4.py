# Импортируем модуль psycopg для связи Python с PostgreSQL
import psycopg

# Это соединение с сервером. Без него запрос не уйдёт
conn = psycopg.connect(
    host="localhost",      # база на этом компьютере
    dbname="books_lab",    # имя базы
    user="postgres",       # пользователь сервера
    password="Admin"  # пароль сервера, не пароль из формы
)

# Это курсор. Через него отправляем SQL
cur = conn.cursor()

# Это отправка запроса. В кавычках тот же текст, что в Query Tool
cur.execute("SELECT * FROM books WHERE Автор = 'Булгаков';")

# Это забирает все строки ответа в список
rows = cur.fetchall()

# Это печатает каждую строку в консоль
for row in rows:
    print(row)

# Это закрывает курсор
cur.close()
# Это закрывает соединение
conn.close()