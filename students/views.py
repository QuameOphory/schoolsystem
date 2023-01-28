from django.shortcuts import render
from django.views import generic
from .models import (
    Student
)
# Create your views here.

class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = "students/students_list.html"

class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'
    template_name = "students/students_detail.html"
