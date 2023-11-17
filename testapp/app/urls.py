from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StudentCardViewSet, CourseViewSet, CourseSemesterViewSet, SemesterViewSet, TeacherViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('student-cards', StudentCardViewSet)
router.register('courses', CourseViewSet)
router.register('course-semesters', CourseSemesterViewSet)
router.register('semesters', SemesterViewSet)
router.register('teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
