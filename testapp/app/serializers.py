from rest_framework import serializers
from .models import Student, StudentCard, Course, CourseSemester, Semester, Teacher


class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCard
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'courses_number', 'students']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class CourseSemesterSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    semester = SemesterSerializer()

    class Meta:
        model = CourseSemester
        fields = ['id', 'course', 'semester', 'start_date', 'end_date']


class TeacherSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'grade', 'courses']
