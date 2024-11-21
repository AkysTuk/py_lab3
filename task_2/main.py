from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Підключення до бази даних SQLite
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Створення базового класу для моделей
Base = declarative_base()


# Опис моделі для таблиці Students
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, grade={self.grade})"


# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сесії для роботи з базою даних
Session = sessionmaker(bind=engine)
session = Session()


# Функція для додавання студента
def insert_student(name, age, grade):
    student = Student(name=name, age=age, grade=grade)
    session.add(student)
    session.commit()
    print(f"Студент {name} доданий.")


# Функція для отримання всіх студентів
def get_all_students():
    students = session.query(Student).all()
    return students


# Основна програма
def main():
    # Додавання студентів
    insert_student('Alice', 20, 'A')
    insert_student('Bob', 22, 'B')
    insert_student('Charlie', 21, 'C')

    # Виведення всіх студентів
    print("Всі студенти:")
    students = get_all_students()
    for student in students:
        print(student)


if __name__ == '__main__':
    main()