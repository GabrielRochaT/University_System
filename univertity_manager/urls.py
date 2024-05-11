
from django.contrib import admin
from django.urls import path
from students_manager import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]

