from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy
# def list_students(request):
#     students = Student.objects.all()
#     return render(request, "students_manager/students_list.html", {'students': students})

class CourseListView(ListView):
    model = Course
class CourseCreateView(CreateView):
    model= Course
    fields= ['name', 'degree', 'id_class']
    success_url = reverse_lazy('course_list')
class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'degree', 'id_class']
    success_url = reverse_lazy('course_list')
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')