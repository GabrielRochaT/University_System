
from django.contrib import admin
from django.urls import path
from students_manager.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from dashboard.views import DashboardTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardTemplateView.as_view(), name='dashboard'),
    path('view_students', StudentListView.as_view(), name="std_list"),
    path('registrate_student', StudentCreateView.as_view(), name="std_registrate"),
    path('update_student/<int:pk>', StudentUpdateView.as_view(), name='std_update'),
    path("delete_student/<int:pk>", StudentDeleteView.as_view(), name="std_delete")
]

