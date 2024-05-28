from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Teacher
from django.urls import reverse_lazy
# def list_students(request):
#     students = Student.objects.all()
#     return render(request, "students_manager/students_list.html", {'students': students})

class TeacherListView(ListView):
    model = Teacher
class TeacherCreateView(CreateView):
    model= Teacher
    fields= ['name', 'register', 'id_course', 'id_class']
    success_url = reverse_lazy('prof_list')
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'register', 'id_course', 'id_class']
    success_url = reverse_lazy('prof_list')
class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('prof_list')