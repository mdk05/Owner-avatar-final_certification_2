import psycopg2

# Подключение к базе данных PostgreSQL
connection = psycopg2.connect(
    host="db",
    database="employees_db",
    user="postgres",
    password="password"
)
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100),
        hire_date DATE
    );
''')
print("Таблица 'employees' создана.")

# Наполнение таблицы данными
cursor.execute('''
    INSERT INTO employees (name, department, hire_date) 
    VALUES 
        ('Alice', 'Engineering', '2021-01-01'),
        ('Bob', 'HR', '2020-07-15'),
        ('Charlie', 'Marketing', '2019-10-30')
    ON CONFLICT DO NOTHING;
''')
connection.commit()
print("Данные добавлены в таблицу 'employees'.")

# Вывод данных из таблицы
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

print("Содержимое таблицы 'employees':")
for row in rows:
    print(row)

# Закрытие соединения
cursor.close()
connection.close()
