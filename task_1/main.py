import sqlite3

# Функція для створення бази даних та таблиці Students
def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("Таблиця Students створена або вже існує.")

# Функція для додавання студента
def insert_student(name, age, grade):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Students (name, age, grade)
    VALUES (?, ?, ?)
    ''', (name, age, grade))

    conn.commit()
    conn.close()
    print(f"Студент {name} доданий.")

# Функція для отримання всіх студентів
def get_all_students():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()

    conn.close()

    return students

# Функція для оновлення віку студента
def update_student_age(student_id, new_age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE Students SET age = ? WHERE id = ?
    ''', (new_age, student_id))

    conn.commit()
    conn.close()
    print(f"Вік студента з id {student_id} оновлено.")

# Функція для видалення студента
def delete_student(student_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM Students WHERE id = ?
    ''', (student_id,))

    conn.commit()
    conn.close()
    print(f"Студент з id {student_id} видалений.")

# Основна програма
def main():
    create_table()  # Створення таблиці

    # Додавання студентів
    insert_student('Alice', 20, 'A')
    insert_student('Bob', 22, 'B')
    insert_student('Charlie', 21, 'C')

    # Виведення всіх студентів
    print("Всі студенти:")
    students = get_all_students()
    for student in students:
        print(student)

    # Оновлення віку студента
    update_student_age(1, 21)  # Оновлення віку студента з id = 1

    # Виведення студентів після оновлення
    print("Студенти після оновлення віку:")
    students = get_all_students()
    for student in students:
        print(student)

    # Видалення студента
    delete_student(2)  # Видалення студента з id = 2

    # Виведення студентів після видалення
    print("Студенти після видалення:")
    students = get_all_students()
    for student in students:
        print(student)

if __name__ == '__main__':
    main()