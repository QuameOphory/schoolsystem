from django.shortcuts import render
from django.views import generic
from .models import (
    Student
)
# Create your views here.

class StudentListView(generic.ListView):
    model = Student
    template_name = "students/students_list.html"

