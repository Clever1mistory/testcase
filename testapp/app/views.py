from rest_framework.viewsets import ModelViewSet
from .models import Student, StudentCard, Course, CourseSemester, Semester, Teacher
from .serializers import StudentSerializer, StudentCardSerializer, CourseSerializer, \
    CourseSemesterSerializer, SemesterSerializer, TeacherSerializer


class StudentViewSet(ModelViewSet):
    """
    ViewSet для модели Student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ['first_name', 'last_name']  # Поля, по которым можно выполнять поиск
    filter_fields = ['first_name', 'last_name']  # Поля, по которым можно выполнять фильтрацию


class StudentCardViewSet(ModelViewSet):
    """
    ViewSet для модели StudentCard
    """
    queryset = StudentCard.objects.all()
    serializer_class = StudentCardSerializer
    search_fields = ['name']  # Поля, по которым можно выполнять поиск
    filter_fields = ['name']  # Поля, по которым можно выполнять фильтрацию


class CourseViewSet(ModelViewSet):
    """
    ViewSet для модели Course
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    search_fields = ['name']  # Поля, по которым можно выполнять поиск
    filter_fields = ['name']  # Поля, по которым можно выполнять фильтрацию


class CourseSemesterViewSet(ModelViewSet):
    """
    ViewSet для модели CourseSemester
    """
    queryset = CourseSemester.objects.all()
    serializer_class = CourseSemesterSerializer
    search_fields = ['start_date', 'end_date']  # Поля, по которым можно выполнять поиск
    filter_fields = ['start_date', 'end_date']  # Поля, по которым можно выполнять фильтрацию


class SemesterViewSet(ModelViewSet):
    """
    ViewSet для модели Semester
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    search_fields = ['semesters_number']  # Поля, по которым можно выполнять поиск
    filter_fields = ['semesters_number']  # Поля, по которым можно выполнять фильтрацию


class TeacherViewSet(ModelViewSet):
    """
    ViewSet для модели Teacher
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    search_fields = ['first_name', 'last_name', 'grade']  # Поля, по которым можно выполнять поиск
    filter_fields = ['grade']  # Поля, по которым можно выполнять фильтрацию
