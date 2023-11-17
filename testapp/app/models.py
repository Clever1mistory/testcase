from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.first_name


class StudentCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_cards')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Карта студента'
        verbose_name_plural = 'Карты студентов'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    courses_number = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class CourseSemester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Семестр курса'
        verbose_name_plural = 'Семестры курсов'


class Semester(models.Model):
    semesters_number = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
