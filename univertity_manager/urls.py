
from django.contrib import admin
from django.urls import path
from students_manager.views import *
from teachers_manager.views import *
from courses_manager.views import *
from classes_manager.views import *
from dashboard.views import DashboardTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardTemplateView.as_view(), name='home'),
    path('view_students', StudentListView.as_view(), name="std_list"),
    path('view_teachers', TeacherListView.as_view(), name='prof_list'),
    path('view_courses', CourseListView.as_view(), name='course_list'),
    path('view_classes', ClassesListView.as_view(), name='class_list'),
    path('registrate_student', StudentCreateView.as_view(), name='std_registrate'),
    path('registrate_teacher', TeacherCreateView.as_view(), name='prof_registrate'),
    path('registrate_course', CourseCreateView.as_view(), name='course_registrate'),
    path('registrate_class', ClassesCreateView.as_view(), name='class_registrate'),
    path('update_student/<int:pk>', StudentUpdateView.as_view(), name='std_update'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='prof_update'),
    path('update_course/<int:pk>', CourseUpdateView.as_view(), name='course_update'),
    path('update_class/<int:pk>', ClassesUpdateView.as_view(), name='class_update'),
    path("delete_student/<int:pk>", StudentDeleteView.as_view(), name="std_delete"),
    path("delete_teacher/<int:pk>", TeacherDeleteView.as_view(), name="prof_delete"),
    path("delete_course/<int:pk>", CourseDeleteView.as_view(), name="course_delete"),
    path("delete_class/<int:pk>", ClassesDeleteView.as_view(), name="class_delete")
]

