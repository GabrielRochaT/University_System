from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Classes
from django.urls import reverse_lazy
class ClassesListView(ListView):
    model = Classes
class ClassesCreateView(CreateView):
    model= Classes
    fields= ['name', 'workload']
    success_url = reverse_lazy('class_list')
class ClassesUpdateView(UpdateView):
    model = Classes
    fields = ['name', 'workload']
    success_url = reverse_lazy('class_list')
class ClassesDeleteView(DeleteView):
    model = Classes
    success_url = reverse_lazy('class_list')