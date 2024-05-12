from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Classes
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
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'register', 'id_course', 'id_class']
    success_url = reverse_lazy('std_list')
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('std_list')