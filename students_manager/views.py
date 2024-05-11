from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Student
from django.urls import reverse_lazy
# def list_students(request):
#     students = Student.objects.all()
#     return render(request, "students_manager/students_list.html", {'students': students})

class StudentListView(ListView):
    model = Student

class StudentCreateView(CreateView):
    model= Student
    fields= ['name', 'register', 'id_course', 'id_class']
    success_url = reverse_lazy('std_list')