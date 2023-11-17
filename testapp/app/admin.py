from django.contrib import admin
from .models import Student, StudentCard, Course, CourseSemester, Semester, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(StudentCard)
class StudentCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'student')
    list_filter = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'courses_number')
    list_filter = ('name', 'courses_number')


@admin.register(CourseSemester)
class CourseSemesterAdmin(admin.ModelAdmin):
    list_display = ('course', 'semester', 'start_date', 'end_date')
    list_filter = ('course', 'semester', 'start_date', 'end_date')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semesters_number',)
    list_filter = ('semesters_number',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade')
    list_filter = ('first_name', 'last_name', 'grade')
