from django.shortcuts import render
from django.views import generic
from django.forms import formset_factory
from .forms import (
    StudentForm, StudentAlertForm, StudentHobbyForm, StudentGuardianForm,
    PreviousEducationForm, StudentFavoriteQuoteForm, IDCardForm, 
    StudentGuardianForm, GuardianForm
)
from .models import (
    Student
)
# Create your views here.

StudentFormset = formset_factory(StudentForm, extra=1)
StudentAlertFormset = formset_factory(StudentAlertForm)
StudentHobbyFormset = formset_factory(StudentHobbyForm)
StudentGuardianFormset = formset_factory(StudentGuardianForm)
PreviousEducationFormset = formset_factory(PreviousEducationForm)
StudentFavoriteQuoteFormset = formset_factory(StudentFavoriteQuoteForm)
IDCardFormset = formset_factory(IDCardForm)
GuardianFormset = formset_factory(GuardianForm)



class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = "students/students_list.html"

class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'
    template_name = "students/students_detail.html"

class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentFormset
    template_name = "students/add_student.html"

    def get(self, request, *args, **kwargs):
        # self.object = None
        student_formset = StudentFormset(prefix = 'students')
        previous_education_formset = PreviousEducationFormset(prefix='previous_educations')
        student_alert_formset = StudentAlertFormset(prefix='student_alerts')
        student_hobby_formset = StudentHobbyFormset(prefix = 'student_hobbies')
        student_guardian_formset = StudentGuardianFormset(prefix='student_guardians')
        favorite_quote_formset = StudentFavoriteQuoteFormset(prefix='favorite_quotes')
        guardian_formset = GuardianFormset(prefix='guardians')
        return self.render_to_response({

                    'student_formset':student_formset,
                    'previous_education_formset':previous_education_formset,
                    'student_alert_formset':student_alert_formset,
                    'student_hobby_formset':student_hobby_formset,
                    'student_guardian_formset':student_guardian_formset,
                    'favorite_quote_formset':favorite_quote_formset,
                    'guardian_formset': guardian_formset
            })
    
    
