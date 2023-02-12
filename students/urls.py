from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView, StudentCreateView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('add/', StudentCreateView.as_view(), name='add_student'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
]
