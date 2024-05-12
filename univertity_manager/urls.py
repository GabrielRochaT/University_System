
from django.contrib import admin
from django.urls import path
from students_manager.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name="std_list"),
    path('registrate', StudentCreateView.as_view(), name="std_registrate"),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='std_update'),
    path("delete/<int:pk>", StudentDeleteView.as_view(), name="std_delete")
]

