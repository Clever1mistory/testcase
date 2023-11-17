import random
from django.utils import timezone
from faker import Faker
from app.models import Student, StudentCard, Course, CourseSemester, Semester, Teacher

fake = Faker()


# Функция для создания случайного студента
def create_student():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return Student.objects.create(first_name=first_name, last_name=last_name)


# Функция для создания случайной карточки студента
def create_student_card(student):
    name = fake.word()
    return StudentCard.objects.create(student=student, name=name)


# Функция для создания случайного курса
def create_course():
    name = fake.word()
    courses_number = random.randint(1, 10)
    return Course.objects.create(name=name, courses_number=courses_number)


# Функция для создания случайного семестра
def create_semester():
    semesters_number = random.randint(1, 10)
    return Semester.objects.create(semesters_number=semesters_number)


# Функция для создания случайного курса семестра
def create_course_semester(course, semester):
    start_date = timezone.now()
    end_date = timezone.now()
    return CourseSemester.objects.create(course=course, semester=semester, start_date=start_date, end_date=end_date)


# Функция для создания случайного преподавателя
def create_teacher():
    first_name = fake.first_name()
    last_name = fake.last_name()
    grade = fake.word()
    return Teacher.objects.create(first_name=first_name, last_name=last_name, grade=grade)


# Создание данных
def seed():
    students = []
    student_cards = []
    courses = []
    semesters = []
    course_semesters = []
    teachers = []

    # Создание студентов и карточек студентов
    for _ in range(10):
        student = create_student()
        students.append(student)
        student_card = create_student_card(student)
        student_cards.append(student_card)

    # Создание курсов
    for _ in range(5):
        course = create_course()
        courses.append(course)

    # Создание семестров
    for _ in range(5):
        semester = create_semester()
        semesters.append(semester)

    # Создание курсов семестра
    for course in courses:
        for semester in semesters:
            course_semester = create_course_semester(course, semester)
            course_semesters.append(course_semester)

    # Создание преподавателей
    for _ in range(5):
        teacher = create_teacher()
        teachers.append(teacher)

    print("Data seeding completed.")

# Вызов функции заполнения данных
seed()
